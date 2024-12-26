import re

def validadorSenha(senha):
    if len(senha) < 8:
        return False
    
    if not re.search(r'[a-z]', senha) or not re.search(r'[A-Z]', senha):
        return False
    
    if not re.search(r'[0-9]', senha):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False
    
    return True

senha1 = "Senha123@"

senha2 = "senhafraca"

senha3 = "Senha_fraca"

print(validadorSenha(senha1))  

print(validadorSenha(senha2)) 

print(validadorSenha(senha3))  