import csv

# with open('dados.csv', 'r') as arquivo:
#     leitor_csv = csv.reader(arquivo)
#     next(leitor_csv)  # pula a primeira linha (cabeçalho)
#     for linha in leitor_csv:
#         if linha[2] == 'Brasil':
#             print(linha)
           
arquivo = open('dados.csv', 'r')
leitor_csv = csv.reader(arquivo)
next(leitor_csv)  # pula a primeira linha (cabeçalho)
for linha in leitor_csv:
    if linha[2] == 'Brasil':
        print(linha)

arquivo.close()