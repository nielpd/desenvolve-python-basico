# exercicio 1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
pares = [num for num in lista if num % 2 == 0]

print(f"lista com numeros pares: {pares}")

# exercicio 2

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [num**2 for num in lista2]

print(f"lista com quadrados: {quadrados}")

# exercicio 3

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
divisiveis = [num for num in lista if num % 7 == 0]

print(f"lista com numeros divisiveis por 7: {divisiveis}")

# exercicio 4

paridade = ["par" if num % 2 == 0 else "impar" for num in range(0, 30, 3)]

print(paridade)

