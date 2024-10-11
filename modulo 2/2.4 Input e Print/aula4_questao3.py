total = 0 
produtos = []

while True:
  nome = input("digite o nome do produto: ")
  precoUnitario = float(input("digite o preço unitário: "))
  quantidade = int(input("digite a quantidade: "))

  produtos.append([nome, precoUnitario, quantidade])

  total += (precoUnitario * quantidade)

  response = input("deseja adicionar mais um produto? (s/n)")
  if response == 's':
    continue
  elif response == 'n':
    break
  else:
    print("Resposta não reconhecida, Fechando a lista de compras...")
    break

print("\nResumo da compra:")
for produto in produtos:
  print(f"{produto[0]} - R$ {produto[1]:.2f} x {produto[2]} = R$ {produto[1] * produto[2]:.2f}")

print(f"Total: R$ {total:.2f}")