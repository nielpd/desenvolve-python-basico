def Tabuada():
  n = int(input("Escolha um digito para multiplicar com 9!: "))
  if (n > 10):
    print("O resultado é:", n * 9)
    return "Fim do programa"
  else:
    def regraMultiplicacao(n):
      s1 = n - 1
      s2 = 10 - n
      result = str(s1) + str(s2)
      print("O resultado é:", result)
      resposta = str(input("Deseja Multiplicar o primeiro algarismo por 10? (s/n)"))
      if resposta == 's':
        return "O resultado é:" + str(s1 * 10) + str(s2)
      elif resposta == 'n':
        return "Fim do programa"
      else:
        return "Resposta não reconhecida, Fim do programa"
    return regraMultiplicacao(n)

print(Tabuada())