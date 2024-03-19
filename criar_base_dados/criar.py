import csv
import random
import json
import pandas as pd
from datetime import datetime, timedelta


# Abre o arquivo 'lista_produtos.json' na pasta do projeto
with open(r'criar_base_dados/lista_produtos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Converte o arquivo json em um pandas.DataFrame
df = pd.DataFrame(data)

# Converte o pandas.DataFrame em um dicionário
lista_produtos = df.set_index('Produto')['Categoria'].to_dict()

# Abre o arquivo 'municipios_uf_brasil.csv' na pasta do projeto
df = pd.read_csv(r'criar_base_dados/municipios_uf_brasil.csv', encoding='utf-8', delimiter=';')

# Converte o pandas.DataFrame em um dicionário
lista_regioes = df.set_index('UF')['MUNICÍPIO'].to_dict()

# Define as datas de início e fim
data_inicial = datetime(2010, 1, 1)
data_final = datetime(2023, 12, 31)

# Define as horas inicial e final
hora_inicial = 9
hora_final = 17

# Nome do arquivo que será salvo
nome_database = "base_dados"

# Local onde o arquivo será salvo
caminho_base_dados = "criar_base_dados/" + nome_database + ".csv"

# Quantidade de Registros que serão criados
total_registros = int(input("Quantidade de Registros: "))

print("\nSerá criado um arquivo com o nome %s com a quantidade de %d registros.\n" %
      (nome_database, total_registros))


# Função para gerar uma data aleatória dentro do intervalo dado
def rd_data():
    # Gera uma data aleatória
    dias_aleatorios = random.randint(0, (data_final - data_inicial).days)
    data_aleatoria = data_inicial + timedelta(days=dias_aleatorios)

    # Garante que a data seja um dia da semana (segunda=0, sexta=4)
    while data_aleatoria.weekday() > 4:  # 0 é segunda, 6 é domingo
        data_aleatoria += timedelta(days=1)

    # Gera um horário comercial aleatório
    hora_aleatoria = random.randint(hora_inicial, hora_final - 1)
    minuto_aleatorio = random.randint(0, 59)
    segundo_aleatorio = random.randint(0, 59)

    # Combina a data e o horário
    data_horario_final = datetime(
        data_aleatoria.year,
        data_aleatoria.month,
        data_aleatoria.day,
        hora_aleatoria,
        minuto_aleatorio,
        segundo_aleatorio
    )
    return data_horario_final


# Função para seleciona aleatoriamente um dos valores em 'lista_produtos'
def rd_produto():
    return random.choice(list(lista_produtos.items()))


# Função para gerar um tipo de transação aleatório
def rd_tipo():
    return random.choice(["Compra", "Venda"])


# Função para gerar um preço aleatório
def rd_valor():
    return round(random.uniform(100, 5000), 2)


def rd_quantidade():
    qtd_maxima = 100
    return random.randint(1, qtd_maxima)


# Função para gerar um custo de aquisição aleatório
def rd_custo(valor_produto):
    valor_maximo = valor_produto * 0.8
    valor_minimo = valor_produto * 0.3
    return round(random.uniform(valor_minimo, valor_maximo), 2)


# Função para gerar um canal de venda aleatório
def rd_canal():
    return random.choice(["Online", "Loja Física", "Distribuidor"])


# Função para gerar um método de pagamento aleatório
def rd_pagamento():
    return random.choice(["Cartão de Crédito", "A Vista", "Boleto", "Transferência Bancária"])


# Função para gerar um método de pagamento aleatório
def rd_regiao():
    return random.choice(list(lista_regioes.items()))


# Cria um arquivo CSV para escrever os dados
with open(caminho_base_dados, mode='w', newline='', encoding='utf-8') as file:
    arquivo = csv.writer(file)

    # Escreve o cabeçalho
    arquivo.writerow(["Data", "Produto", "Categoria", "Quantidade", "Tipo", "Valor Unitário",
                      "Custo", "Canal de Venda", "Método de Pagamento", "Estado", "Município"])

    # Gera as linhas de dados
    for i in range(total_registros):
        data = rd_data()
        produto, categoria_produto = rd_produto()
        quantidade = rd_quantidade()
        tipo = rd_tipo()
        valor_unitario = rd_valor()
        custo = rd_custo(valor_unitario)
        canal = rd_canal()
        pagamento = rd_pagamento()
        municipio, estado = rd_regiao()

        # Cria a estrutura para salvar
        registro = [data, produto, categoria_produto, quantidade, tipo,
                    valor_unitario, custo, canal, pagamento, municipio, estado]

        # Exibe a informação que será salva no arquivo
        print("\tRegistro %d: %s." % (i + 1, registro))

        # Escreve a linha no arquivo CSV
        arquivo.writerow(registro)

print("Processo de ordenação da base de dados...")

# Abre o arquivo gerado
df = pd.read_csv(r''+caminho_base_dados, encoding='utf-8')

# Ordena a coluna de acordo com o atributo 'Data' e refaz o indice
df = df.sort_values(['Data'], ignore_index=True)

# Converte a data para o formato pandas.datetime
df['Data'] = pd.to_datetime(df['Data'])

# Salva o arquivo após tratamento
df.to_csv(r''+caminho_base_dados, index=False, encoding='utf-8')

print("Processo finalizado com sucesso!")
