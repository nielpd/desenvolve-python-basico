def CalcularPrecoFrete(Distancia, Peso):
  if Distancia <= 100:
    PrecoPorKG = 1.0
  elif Distancia >= 100 and Distancia <= 300:
    PrecoPorKG = 1.5
  else:
    PrecoPorKG = 2.0

  ValorFrete = PrecoPorKG * Peso

  if Peso > 10:
    ValorFrete += 10

  return ValorFrete

Distancia = float(input("Qual a distância da viagem? (Em KM) "))
Peso = float(input("Qual o peso da carga? (Em KG) "))
print(f"O valor do frete é de {CalcularPrecoFrete(Distancia, Peso):.2f}")  