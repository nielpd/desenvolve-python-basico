EscolhaClasse = str(input("Qual a sua escolha de classe? | Guerreiro (1) | Mago (2) | Arqueiro (3) | "))

if EscolhaClasse == "1" or EscolhaClasse.lower() == "guerreiro":
    print("Parabéns pela escolha -> Guerreiro")
    PontosRestantes = 50

    print(f"Você tem {PontosRestantes} pontos para distribuir: | Força | Mana | Inteligência | Sabedoria |")
    
    PontoForca = int(input("Força: "))
    PontosRestantes -= PontoForca
    print(f"Pontos restantes: {PontosRestantes}")

    PontoMana = int(input("Mana: "))
    PontosRestantes -= PontoMana
    print(f"Pontos restantes: {PontosRestantes}")

    PontoInteligencia = int(input("Inteligência: "))
    PontosRestantes -= PontoInteligencia
    print(f"Pontos restantes: {PontosRestantes}")

    PontoSabedoria = int(input("Sabedoria: "))
    PontosRestantes -= PontoSabedoria
    print(f"Pontos restantes: {PontosRestantes}")

    result = PontoForca >= 15 and PontoMana <= 10
    print(f"Atributos válidos para Guerreiro: {result}")

elif EscolhaClasse == "2" or EscolhaClasse.lower() == "mago":
    print("Parabéns pela escolha -> Mago")
    PontosRestantes = 50

    print(f"Você tem {PontosRestantes} pontos para distribuir: | Força | Mana | Inteligência | Sabedoria |")

    PontoForca = int(input("Força: "))
    PontosRestantes -= PontoForca
    print(f"Pontos restantes: {PontosRestantes}")

    PontoMana = int(input("Mana: "))
    PontosRestantes -= PontoMana
    print(f"Pontos restantes: {PontosRestantes}")

    PontoInteligencia = int(input("Inteligência: "))
    PontosRestantes -= PontoInteligencia
    print(f"Pontos restantes: {PontosRestantes}")

    PontoSabedoria = int(input("Sabedoria: "))
    PontosRestantes -= PontoSabedoria
    print(f"Pontos restantes: {PontosRestantes}")

    result = PontoForca <= 10 and PontoMana >= 15
    print(f"Atributos válidos para Mago: {result}")

elif EscolhaClasse == "3" or EscolhaClasse.lower() == "arqueiro":
    print("Parabéns pela escolha -> Arqueiro")
    PontosRestantes = 50

    print(f"Você tem {PontosRestantes} pontos para distribuir: | Força | Mana | Inteligência | Sabedoria |")

    PontoForca = int(input("Força: "))
    PontosRestantes -= PontoForca
    print(f"Pontos restantes: {PontosRestantes}")

    PontoMana = int(input("Mana: "))
    PontosRestantes -= PontoMana
    print(f"Pontos restantes: {PontosRestantes}")

    PontoInteligencia = int(input("Inteligência: "))
    PontosRestantes -= PontoInteligencia
    print(f"Pontos restantes: {PontosRestantes}")

    PontoSabedoria = int(input("Sabedoria: "))
    PontosRestantes -= PontoSabedoria
    print(f"Pontos restantes: {PontosRestantes}")

    result = 5 < PontoForca <= 15 and 5 < PontoMana <= 15
    print(f"Atributos válidos para Arqueiro: {result}")

else:
    print("Classe não existente, escolha inválida.")
