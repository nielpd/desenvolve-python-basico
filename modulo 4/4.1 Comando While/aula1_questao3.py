n1 = int(input("digite um valor para N1: "))
n2 = int(input("digite um valor para N2: "))
n3 = int(input("digite um valor para N3: "))

m = (n1 + n2 + n3 ) / 3 

if m >= 60:
  print("aprovado")
elif m >= 40:
  print("Recuperação")
else: 
  print("reprovado")

print("Fim")