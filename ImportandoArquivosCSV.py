"""Este é um arquivo criado para realizar a importação de um arquivo no formato CSV e realizar a leitura."""
import csv

with open('arquivoCSV.csv', 'r', encoding='utf8') as arquivo:
    # Carrega um arquivo CSV para a memória, com delimitador de virgula
    arquivo_csv = csv.reader(arquivo, delimiter=",")

    # Não faz nada (pelo menos ainda)
    n = 0

    
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Região: " + str(linha))
        else:
            print("ID: " + str(linha))