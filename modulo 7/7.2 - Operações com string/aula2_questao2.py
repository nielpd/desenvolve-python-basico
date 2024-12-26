vogais = "aeiou"

frase = input(str("Digite uma frase: "))

substituirVogais = [char if char not in vogais else "*" for char in frase]

print("".join(substituirVogais))