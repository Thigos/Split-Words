import librosa
import librosa.display
import os
import numpy as np
#import matplotlib.pyplot as plt
import soundfile as sf
import organizarAudios
from pydub import AudioSegment

cropped = False

def procurarAmplInicial(y, amplInicial):
    for ampl in y:
        if ampl > amplInicial:
            position = np.array(list(map(np.int, np.where(y == ampl)[0])))
            return position[0]
    
def procurarAmplFinal(y, sr):
    global cropped
    time = []
    ampls = []
    for numAmpl in y:
        if numAmpl <= 0.0130:
            if numAmpl > 0:
                ampls.append(numAmpl)
                time.append(numAmpl)
                #print(ampls[-1]) #Debugger

        #Se ele tiver 3000 amplitudes (0,13s em um audio de 10s) consecutivas menores que 0.0130 então ele tem um silêncio
        elif len(ampls) >= 3000:
            position = np.array(list(map(np.int, np.where(y == ampls[-1])[0])))
            print('\n\nPosição:', position[0], '\nAmpl:', ampls[-1], '\nEixo X:', len(time)/sr)
            cropped = True
            return position[0]

        else:
            ampls = []

def speedChange(sound, speed=1.0):
	sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
	    "frame_rate": int(sound.frame_rate * speed)
	})
	return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    

diret = os.path.dirname(os.path.abspath(__file__))

#Diminuir veloc do som, caso as frases sejam pronunciadas rapidamente (1.0 = Velocidade Padrão)
sound = AudioSegment.from_wav("audio.wav")
slow_sound = speedChange(sound, 1.0)

out_filename = "temp.wav"
slow_sound.export(out_filename, format="wav")

#Carregar som

y, sr = librosa.load(diret + '/temp.wav')
duration = librosa.get_duration(y, sr)

#Quanto vale 1s
segundo = duration/sr
count = 0.0

print(duration)


while count <= duration:
    print('\nContagem:' , count)
    #Retirar Silêncio inicial (Imagem: 01)
    y = y[procurarAmplInicial(y=y, amplInicial=0.0130):]

    #Retirar Silêncio final da frase (Imagem: 02)
    final = procurarAmplFinal(y,sr)
    cropAud = y[:final]

    """librosa.display.waveplot(y, sr=sr, alpha=0.25)
    plt.tight_layout()
    plt.show()"""
    if cropped:
        out_filename = diret + "/Falas/" + str(count) + "_Audio.wav"
        sf.write(out_filename, cropAud, sr, 'PCM_24')
        cropped = False
    else:
        break

    #Excluir parte salva do audio
    y = y[final:]

    count += segundo


organizarAudios.organizar()
