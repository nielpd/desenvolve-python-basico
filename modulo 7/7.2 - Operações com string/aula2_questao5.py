import random

def embaralharPalavras(frase):
    palavras = frase.split()  
    palavrasEmbaralhadas = []

    for palavra in palavras:
        if len(palavra) > 3:
            inicio, meio, fim = palavra[0], palavra[1:-1], palavra[-1]
            meio = list(meio)
            random.shuffle(meio)  # Embaralha as letras do meio
            palavraEmbaralhada = inicio + ''.join(meio) + fim
        else:
            palavraEmbaralhada = palavra
        palavrasEmbaralhadas.append(palavraEmbaralhada)

    return ' '.join(palavrasEmbaralhadas) 


frase = "Python é uma linguagem de programação"
resultado = embaralharPalavras(frase)

print(resultado)
