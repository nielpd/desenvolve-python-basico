def calcularDigito(cpf, multiplicadores):
    soma = sum(int(digito) * peso for digito, peso in zip(cpf, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validarCpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf == cpf[0] * 11:
        return False

    primeiroDigito = calcularDigito(cpf[:9], range(10, 1, -1))
    segundoDigito = calcularDigito(cpf[:9] + str(primeiroDigito), range(11, 1, -1))

    return cpf[-2:] == f"{primeiroDigito}{segundoDigito}"

cpfInput = input("Digite um CPF (formato XXX.XXX.XXX-XX): ")

if validarCpf(cpfInput):
    print("Válido")
else:
    print("Inválido")
