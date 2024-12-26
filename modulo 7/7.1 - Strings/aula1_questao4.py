def formatarNumero(numero):
    if len(numero) == 8:
        numero = "9" + numero
    elif len(numero) == 9 and numero[0] != "9":
        return "Numero inválido. Deve começar com 9 se tiver 9 digitos"
    return f"{numero[:5]}-{numero[5:]}"

numero = input(str("Digite o telefone: "))

print(f"Telefone formatado: {formatarNumero(numero)}")