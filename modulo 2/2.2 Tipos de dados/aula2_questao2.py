#Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
  #Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.
  #Some os valores da segunda e terceira variável e armazene em outra variável.
  #Imprima todas as variáveis na ordem de criação e imprima também seus tipos.
result = "O resultado é:"
x = 10
y = 3.5
soma = x + y
print(result, soma)

response = input("Deseja ver os tipos das variaveis? (s/n)")
if response == 's':
  print("variavel x", type(x))
  print("variavel y", type(y))
  print("variavel soma", type(soma))
elif response == 'n':
  print("Fim do programa")
else:
  print("Resposta não reconhecida, Fim do programa")

  