import sys, re

arquivo_origem = "nomes.txt"
arquivo_destino = "palavras.txt"

with open(arquivo_origem, "r") as file:
    conteudo = file.read()
    
palavras = re.findall(r'\b[A-Za-z]+\b', conteudo)

with open(arquivo_destino, "w") as file:
    for palavra in palavras:
        file.write(palavra + "\n")

    print(f"frase salva em {sys.path[0]}/{arquivo_destino}")    

# caso der o erro: FileNotFoundError significa que o arquivo não existe ou não foi encontrado, 
# rode o script da questão 1 primeiro ou crie o arquivo