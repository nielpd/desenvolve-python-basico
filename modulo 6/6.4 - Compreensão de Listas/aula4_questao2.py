frase = input(str("Digite uma frase: "))

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vogaisFrase = [i for i in frase if i in vogais]

consoantesFrase = [i for i in frase if i in consoantes]

print(sorted(vogaisFrase))
print(sorted(consoantesFrase))

