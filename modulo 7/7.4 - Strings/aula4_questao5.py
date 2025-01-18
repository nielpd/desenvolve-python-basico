import csv

header = ['Titulo', 'Autor','Ano', 'Páginas']
dados = [
    ['O Senhor dos Aneis', 'J. R. R. Tolkien', 1954, 432],  
    ['Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997, 423],
    ['1984', 'George Orwell', 1949, 328],
    ['O Apanhador no Campo de Centeio', 'J.D. Salinger', 1951, 192],
    ['O Conto de Fadas', 'Neil Gaiman', 1990, 272],
    ['O Homem que Calculava', 'Malba Tahan', 1938, 288],
    ['O Poderoso Chefão', 'Mario Puzo', 1969, 416],
    ['O Processo', 'Franz Kafka', 1925, 272],
    ['Dom Quixote', 'Miguel de Cervantes', 1605, 880],
    ['Uma Breve História do Tempo', 'Stephen Hawking', 1988, 240],
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(dados)

print("Arquivo CSV criado e dados inseridos com sucesso!")