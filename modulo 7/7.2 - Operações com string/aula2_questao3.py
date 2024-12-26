import re

def Palindromo(frase):
    fraseLimpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    return fraseLimpa == fraseLimpa[::-1]

print('Digite uma frase (digite "fim" para encerrar):')

while True:
    entradaUsuario = input()
    
    if entradaUsuario.strip().lower() == 'fim':
        break
    
    if Palindromo(entradaUsuario):
        print(f'"{entradaUsuario}" é palíndromo')
    else:
        print(f'"{entradaUsuario}" não é palíndromo')
