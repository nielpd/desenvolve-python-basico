def ObterLista(NomeLista, Tamanho):
    Lista = []
    print(f"Digite os {Tamanho} elementos da {NomeLista}:")
    for _ in range(Tamanho):
        Elemento = int(input())
        Lista.append(Elemento)
    return Lista

def IntercalarListas(Lista1, Lista2):
    ListaIntercalada = []
    for i in range(min(len(Lista1), len(Lista2))):
        ListaIntercalada.append(Lista1[i])
        ListaIntercalada.append(Lista2[i])
    ListaIntercalada.extend(Lista1[i+1:] if len(Lista1) > len(Lista2) else Lista2[i+1:])
    return ListaIntercalada

TamanhoLista1 = int(input("Digite a quantidade de elementos da lista 1: "))
Lista1 = ObterLista("lista 1", TamanhoLista1)

TamanhoLista2 = int(input("Digite a quantidade de elementos da lista 2: "))
Lista2 = ObterLista("lista 2", TamanhoLista2)

ListaIntercalada = IntercalarListas(Lista1, Lista2)
print("Lista intercalada:", *ListaIntercalada)