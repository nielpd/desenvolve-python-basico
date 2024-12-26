import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    
    def criptografar_nome(nome, chave):
        return ''.join(
            chr(((ord(c) - 33 + chave) % 94) + 33) if 33 <= ord(c) <= 126 else c
            for c in nome
        )
    
    nomes_criptografados = [criptografar_nome(nome, chave) for nome in nomes]
    
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
