import random

NumElementos = random.randint(5, 20)
Elementos = [random.randint(1, 10) for _ in range(NumElementos)]

Soma = sum(Elementos)
Media = Soma / NumElementos

print(f"Elementos: {Elementos}")
print(f"Soma: {Soma}")
print(f"Media: {Media}")