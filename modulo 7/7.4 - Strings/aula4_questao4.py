import random

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar_forca():
    with open("gabarito_forca.txt", "r") as f:
        palavras = f.read().splitlines()
    
    with open("enforcado.txt", "r") as f:
        estagios = f.read().split("\n\n")
    
    palavra = random.choice(palavras)
    palavra_oculta = ["_" for _ in palavra]
    
    tentativas = 6
    erros = 0
    letras_erradas = []
    
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    
    while erros < tentativas and "_" in palavra_oculta:
        print("\nPalavra: ", " ".join(palavra_oculta))
        print("Letras erradas: ", ", ".join(letras_erradas))
        imprime_enforcado(erros, estagios)
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print("Boa! Você acertou uma letra.")
        else:
            erros += 1
            letras_erradas.append(letra)
            print("Ops! Você errou.")
    
    if "_" not in palavra_oculta:
        print("\nParabéns! Você acertou a palavra:", palavra)
    else:
        imprime_enforcado(erros, estagios)
        print("\nVocê foi enforcado! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_forca()
