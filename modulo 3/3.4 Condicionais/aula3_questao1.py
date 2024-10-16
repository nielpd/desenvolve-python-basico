n1, n2 = int(input("digite um valor:")), int(input("digite outro valor:"))
result = n1 + n2

print(f"{result} é par" if result % 2 == 0 else f"{result} é impar")