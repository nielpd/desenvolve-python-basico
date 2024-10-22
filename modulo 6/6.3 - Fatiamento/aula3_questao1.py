def ObterLista(NomeLista, Tamanho):
    if Tamanho < 4:
        print("O tamanho da lista deve ser maior ou igual a 4.")
        return 
    else:
        Lista = []
        print(f"Digite os {Tamanho} elementos da {NomeLista}:")
        for _ in range(Tamanho):
            Elemento = int(input())
            Lista.append(Elemento)
        return Lista

TamanhoLista = int(input("Digite a quantidade de elementos da lista: "))
Lista = ObterLista("lista", TamanhoLista)

if Lista:
    print("Lista Formada: ", *Lista)
    print("3 Primeiros elementos: ", Lista[:3])
    print("2 Últimos elementos: ", Lista[-2:])
    print("Elementos nas posições pares:", Lista[::2])
    print("Elementos nas posições ímpares:", Lista[1::2])
