# Divisor de Palavras

### Requisitos:

| Nome         | Versão <br> recomendada|
|----------------|------|
| [Python](https://www.python.org/downloads/) | 3.6+ |
| [librosa](https://pypi.org/project/librosa/) | 0.8.1 |
| [pydub](https://pypi.org/project/pydub/) | 0.25.1 |
| [numpy](https://pypi.org/project/numpy/) | 1.21.2 |
| [SoundFile](https://pypi.org/project/SoundFile/) | 0.10.3.post1 |

### Funcionamento:


A função ```procurarAmplInicial()``` buscará a primeira amplitude que seja maior que 0.0130 (≈ -37db) e cortará a lista de amplitudes nessa posição.
<br>
![Imagem01](Imagens/Imagem%2001.png)
<br>
<br>
Na função ```procurarAmplFinal()```, ao detectar 3000 ou mais amplitudes menores que 0.0130 é reconhecido um "silêncio". Assim  o programa cortará a lista de amplitudes.
<br>
![Imagem02](Imagens/Imagem%2002.png)
<br>
<br>
O que ficar entre ```procurarAmplInicial()``` e ```procurarAmplFinal()```, será uma fala.
O programa pode separar palavras ou frases, dependendo da velocidade de pronúncia da pessoa. Caso seja necessário, use a função para desacelerar/acelerar ```speedChange()```.

<br>
<br>
<br>
<br>
<br>
<br>


```ㅤㅤ¯\_(ツ)_/¯ㅤㅤ```
