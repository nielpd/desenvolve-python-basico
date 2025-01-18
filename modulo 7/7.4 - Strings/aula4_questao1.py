import sys

start = input(str("Digite uma frase:"))
nome_arquivo = "nomes.txt"

with open(nome_arquivo, "a") as file:
    file.write(start)
    print(f"frase salva em {sys.path[0]}/{nome_arquivo}")