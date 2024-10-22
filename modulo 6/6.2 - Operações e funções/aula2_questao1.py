import random

def GerarLista():
    Lista = [] 
    for i in range(20):
        num = random.randint(-100, 100)
        Lista.append(num)

    return Lista

ListaGerada = GerarLista()

print("Lista gerada:  ", ListaGerada)
print("Lista ordenada:  ", sorted(ListaGerada))
print("Maior indice: ", max(enumerate(ListaGerada), key=lambda x: x[1]))
print("Menor indice: ", min(enumerate(ListaGerada), key=lambda x: x[1]))
