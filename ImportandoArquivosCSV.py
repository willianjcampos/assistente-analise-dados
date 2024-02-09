import csv

with open("arquivo.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    n = 0
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Região: " + str(linha))
        else:
            print("ID: " + str(linha))