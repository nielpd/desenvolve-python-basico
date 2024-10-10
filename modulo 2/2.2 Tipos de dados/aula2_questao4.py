# Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis. 
saldo = 500
juros = 0.01

for i in range(3):
  saldo = saldo + (saldo * juros)

print("seu novo saldo após 3 meses é:", saldo)