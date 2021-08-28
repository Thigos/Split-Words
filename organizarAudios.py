import os

def organizar():
    arq = []
    for file in os.listdir('Falas'):
        file = file.split('_')[0]
        arq.append(float(file))

    arq.sort()
    count = 0
    for audio in arq:
        os.rename('Falas/' + str(audio) + '_Audio.wav', 'Falas/'+str(count) + '.wav')
        print(audio)
        count += 1
