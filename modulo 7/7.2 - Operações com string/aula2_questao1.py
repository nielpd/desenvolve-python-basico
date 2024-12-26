meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", 
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

response = input(str("Digite sua data de nascimento(dd/mm/aaaa'): "))

dia, mes, ano = response.split("/")
print(f"{dia} de {meses[int(mes)]} de {ano}")