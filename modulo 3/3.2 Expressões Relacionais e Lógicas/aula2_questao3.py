PerguntaIdade = int(input("Qual a sua idade?:"))
PerguntaJogo = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? (s/n):").lower() == 's')
PerguntaVitoria = int(input("Quantos jogos já ganhou?:"))

result = PerguntaIdade >= 18 and PerguntaJogo and PerguntaVitoria >= 2

TraduzirBoolean = {
  True: "Você está apto a ingressar no clube de jogos de tabuleiro, parabéns!",
  False: "Sentimos muito, mas você não está apto a ingressar no clube de jogos de tabuleiro, Pratique mais"
}

print(TraduzirBoolean[result])