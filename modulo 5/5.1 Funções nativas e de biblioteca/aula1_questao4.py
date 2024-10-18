from datetime import datetime

now = datetime.now()

DataAtual = now.strftime("%d/%m/%Y")
HoraAtual = now.strftime("%H:%M:%S")

print(f"Data: {DataAtual}\nHora:{HoraAtual}")