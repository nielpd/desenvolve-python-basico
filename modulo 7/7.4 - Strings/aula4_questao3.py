import re

def contar_personagem(texto, nome_personagem):
    padrao = re.compile(r'\b' + re.escape(nome_personagem) + r'\b', re.IGNORECASE)
    return len(padrao.findall(texto))

with open('roteiro.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    print("Primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())

    print(f"\nNúmero total de linhas: {len(linhas)}")
    maior_linha = max(linhas, key=len)
    print(f"\nA linha com maior número de caracteres tem {len(maior_linha)} caracteres.")
    
    texto_completo = ''.join(linhas)
    contagem_nonato = contar_personagem(texto_completo, "Nonato")
    contagem_iria = contar_personagem(texto_completo, "Íria")
    
    print(f"\nNúmero de menções a 'Nonato': {contagem_nonato}")
    print(f"Número de menções a 'Íria': {contagem_iria}")
