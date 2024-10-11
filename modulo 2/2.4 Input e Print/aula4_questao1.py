comprimento = int(input("digite o comprimento do terreno: "))
largura = int(input("digite a largura do terreno: "))
precoM2 = float(input("Preço por metro quadrado: "))

Area = comprimento * largura

Preco = Area * precoM2

print(f"O terreno tem {Area} m2 e vai custar {Preco:,.2f} reais")