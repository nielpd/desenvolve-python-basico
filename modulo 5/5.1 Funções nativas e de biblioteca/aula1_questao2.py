import random
import math

n = int(input("Insira quantidade de algarismos aleatorios: "))
soma = 0

for i in range(n):
  x = random.randint(0, 100)
  print(x)
  soma += x

print(f"A soma dos números aleatórios é: {soma}")
response = str(input("Deseja calcular a raiz da soma dos numeros? (s/n):  "))
if response == 's':
  result = math.sqrt(soma)
  print("O resultado é:", result)
elif response == 'n':
  print("Fim do programa")
else:
  print("Resposta não reconhecida, Fim do programa")