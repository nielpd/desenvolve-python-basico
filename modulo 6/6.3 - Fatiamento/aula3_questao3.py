import random

lista = [random.randint(-10, 10) for _ in range(20)]

TamanhoFatiaAtual, TamanhoMaiorFatia = 0, 0
InicioFatiaAtual, InicioFatiaMaior = 0, 0

for i in range(len(lista)):
  if lista[i] < 0:
    TamanhoFatiaAtual += 1
    if TamanhoFatiaAtual > TamanhoMaiorFatia:
      TamanhoMaiorFatia = TamanhoFatiaAtual
      InicioFatiaMaior = i - TamanhoFatiaAtual + 1
  else:
    TamanhoFatiaAtual = 0

print("Lista: ", lista)
print(f"O tamanho da maior fatia é {TamanhoMaiorFatia} e comecará na posição {InicioFatiaMaior}")
del lista[InicioFatiaMaior:InicioFatiaMaior + TamanhoMaiorFatia]
print("Lista sem a maior fatia: ", lista)