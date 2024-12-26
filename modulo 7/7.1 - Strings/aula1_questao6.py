frase = input(str("Digite uma frase: "))
fraseObjetivo = input(str("Digite a frase objetivo: "))

def anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

palavras = frase.split()

anagrama = [palavra for palavra in palavras if anagramas(palavra, fraseObjetivo)]

print(anagrama)

print(frase.find(fraseObjetivo))