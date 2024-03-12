import pandas as pd

"""Método que recebe um arquivo JSON e converte em um arquivo CSV"""
def json_to_csv(json_file, csv_file):
    data = pd.read_json(json_file)
    data.to_csv(csv_file, index=False, encoding='utf-8')

# Executa o método json_to_csv para teste
#json_to_csv('arquivoJSON.json', 'arquivoCSV.csv')


"""Método que recebe um arquivo CSV e converte em um arquivo JSON"""
def csv_to_json(csv_file, json_file):
    data = pd.read_csv(csv_file)
    data.to_json(json_file, force_ascii=False, orient='records', indent=4)

# Executa o método csv_to_json para teste
csv_to_json('arquivoCSV.csv', 'arquivoJSON-teste.json')
