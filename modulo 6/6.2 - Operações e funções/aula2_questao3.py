import random
from collections import Counter

lista1, lista2 = [random.randint(0, 50) for _ in range(20)], [random.randint(0, 50) for _ in range(20)]

insercao = sorted(set(lista1).intersection(lista2))

ContagemL1 = Counter(lista1)
ContagemL2 = Counter(lista2)

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista de interseção: ", insercao)

print(f"\nContagem: ")
for elemento in insercao:
  print(f"{elemento}: (lista1={ContagemL1[elemento]}, lista2={ContagemL2[elemento]})")