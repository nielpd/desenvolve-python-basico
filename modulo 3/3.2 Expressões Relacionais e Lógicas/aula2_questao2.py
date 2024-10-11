# Forma que eu gostaria de fazer :P
  # Grupo = [
  #     {'nome': 'João', 'idade': 15},
  #     {'nome': 'Maria', 'idade': 16},
  #     {'nome': 'Jose', 'idade': 17},
  #     {'nome': 'Pedro', 'idade': 11}
  # ]

  # Passe = any(pessoa['idade'] >= 18 for pessoa in Grupo)

IdadeFulaninho = int(input("Fulaninho, Digite sua idade:"))
IdadeCiclaninho = input("Ciclaninho, Digite sua idade:")

Passe = IdadeFulaninho >= 18 or IdadeCiclaninho >= 18

TraduzirBoolean = {
  True: "O grupo possui responsavel, o grupo pode entrar",
  False: "Ninguém do grupo tem mais de 18 anos, o grupo não pode entrar"
}

print(TraduzirBoolean[Passe])