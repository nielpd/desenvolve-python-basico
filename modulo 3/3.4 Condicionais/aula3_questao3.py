def VerificarAnoBissexto(anoBissexto):
  if (AnoBissexto % 4 == 0) and (AnoBissexto % 100 != 0) or (AnoBissexto % 400 == 0):
    return "O ano é bissexto"
  else:
    return "O ano não é bissexto"
  
AnoBissexto = int(input("digite um ano: "))

resultado = VerificarAnoBissexto(AnoBissexto)

print(resultado)