# FilmeNome = str(input("Qual o nome do filme? "))

# NotaMensagem = {
#   1: "Ruim",
#   2: "Regular",
#   3: "Bom",
#   4: "Muito bom",
#   5: "Excelente",
# }

# FilmeNota = int(input("Qual a nota do filme? "))

# print(f"Você avaliou {FilmeNome} como {NotaMensagem[FilmeNota]}")

FilmeNome = str(input("Qual o nome do filme? "))
FilmeNota = int(input("Qual a nota do filme? "))

if FilmeNota == 1:
    print(f"Você avaliou {FilmeNome} como muito ruim")
elif FilmeNota == 2:
    print(f"Você avaliou {FilmeNome} como regular")
elif FilmeNota == 3:
    print(f"Você avaliou {FilmeNome} como bom")
elif FilmeNota == 4:
    print(f"Você avaliou {FilmeNome} como muito bom")
elif FilmeNota == 5:
    print(f"Você avaliou {FilmeNome} como excelente")
else:
    print("Nota inválida")