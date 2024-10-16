n = int(input("Numero de Respondentes: "))
Responentes = 0
SomaIdades = 0
while Responentes < n :
  IdadeRespondente = int(input(f"Idade do Respondente{Responentes + 1}: "))
  SomaIdades += IdadeRespondente
  Responentes += 1  

MediaIdades = SomaIdades / n
print(f"A media das idades dos {n} respondentes é: {MediaIdades}")