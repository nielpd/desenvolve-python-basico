frase = input(str("Digite uma frase: "))

vogais = "aeiou"

indiceVogais = [i for i, char in enumerate(frase) if char.lower() in vogais]

print(indiceVogais)

