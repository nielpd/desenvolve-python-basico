import random

n = int(input("advinhe um número entre 1 e 10: "))
randomN = random.randint(0, 10)

while n != randomN:
  if n > randomN:
    print("Muito alto, tente novamente!")
  n = int(input("advinhe um número entre 1 e 10: "))
else:
    print("Muito baixo, tente novamente!")
    n = int(input("advinhe um número entre 1 e 10: "))

print("Parabens, voce acertou!")