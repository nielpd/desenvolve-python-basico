quantiaDinheiro = int(input("Quantia de dinheiro: "))
notas =[100, 50, 20, 10, 5, 2, 1]

for nota in notas:
  quantidade = quantiaDinheiro // nota
  print(f"{quantidade} nota(s) de R$ {nota}")
  quantiaDinheiro = quantiaDinheiro % nota