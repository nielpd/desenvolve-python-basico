import random
Lista = [] 

for i in range(20):
  num = random.randint(-100, 100)
  Lista.append(num)

print("Lista ordenada:  ", sorted(Lista))
print("Lista gerada:  ", Lista)
print("Maior indice: ", Lista.index(max(Lista)))
print("Menor indice: ", Lista.index(min(Lista)))
