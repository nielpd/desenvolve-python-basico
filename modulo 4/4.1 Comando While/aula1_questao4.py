n = int(input("Insira quantidade de algarismos a serem comparados: "))
maior = 0 

while n > 0:
  x = int(input("Insira um valor para comparar : "))
  if x > maior:
    maior = x
    n -= 1

print("O maior valor inserido foi:", maior)