nome = input(str("Digite seu nome: "))

for letra in range(1, len(nome)):
    print(nome[:letra])
