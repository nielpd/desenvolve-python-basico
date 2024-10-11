idadeJuliana = int(input("Juliana, digite a sua idade: "))
idadeCris = int(input("Cris, digite a sua idade: "))

Passe = idadeJuliana and idadeCris >= 18

TraduzirBoolean = {
  True: "As duas podem entrar juntas",
  False: "Um ou ambos não podem entrar"
}

print(TraduzirBoolean[Passe])