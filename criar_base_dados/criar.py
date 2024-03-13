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

# Define as regiões que podem ser efetuadas as vendas
regioes = ["Goiás", "Minas Gerais", "Mato Grosso"]

# Define as datas de início e fim
data_inicial = datetime(2010, 1, 1)
data_final = datetime(2023, 12, 31)

# Nome do arquivo que será salvo
nome_database = input("Informe o nome da base de dados: ")

# Local onde o arquivo será salvo
caminho_base_dados = "criar_base_dados/" + nome_database + ".csv"

# Quantidade de Registros que serão criados
total_registros = int(input("Tamanho da base de dados: "))

print("\nSerá criado um arquivo com o nome %s com a quantidade de %d registros.\n" %
      (nome_database, total_registros))


# Função para gerar uma data aleatória dentro do intervalo dado
def data_hora_aleatoria(dt_inicial, dt_final, h_inicial, h_final):
    # Gera uma data aleatória
    dias_aleatorios = random.randint(0, (dt_final - dt_inicial).days)
    data_aleatoria = dt_inicial + timedelta(days=dias_aleatorios)

    # Garante que a data seja um dia da semana (segunda=0, sexta=4)
    while data_aleatoria.weekday() > 4:  # 0 é segunda, 6 é domingo
        data_aleatoria += timedelta(days=1)

    # Gera um horário comercial aleatório
    hora_aleatoria = random.randint(h_inicial, h_final - 1)
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


# Função para gerar um tipo de transação aleatório
def tipo_compra_venda():
    return random.choice(["Compra", "Venda"])


# Função para gerar um preço aleatório
def valor_aleatorio():
    return round(random.uniform(100, 5000), 2)


# Função para gerar um custo de aquisição aleatório
def custo_aqusicao(valor_produto):
    valor_maximo = valor_produto * 0.8
    valor_minimo = valor_produto * 0.3
    return round(random.uniform(valor_minimo, valor_maximo), 2)


# Função para gerar um canal de venda aleatório
def tipo_compra_aleatoria():
    return random.choice(["Online", "Loja Física", "Distribuidor"])


# Função para gerar um método de pagamento aleatório
def tipo_pagamento_aleatorio():
    return random.choice(["Cartão de Crédito", "Boleto", "Transferência Bancária"])


# Cria um arquivo CSV para escrever os dados
with open(caminho_base_dados, mode='w', newline='', encoding='utf-8') as file:
    arquivo = csv.writer(file)

    # Escreve o cabeçalho
    arquivo.writerow(["Data", "Produto", "Categoria", "Quantidade", "Tipo", "Valor Unitário",
                      "Custo de Aquisição", "Canal de Venda", "Método de Pagamento", "Estado"])

    # Gera as linhas de dados
    for i in range(total_registros):
        data = data_hora_aleatoria(data_inicial, data_final, 9, 17)
        produto, categoria_produto = random.choice(
            list(lista_produtos.items()))
        quantidade = random.randint(1, 100)
        tipo = tipo_compra_venda()
        valor_unitario = valor_aleatorio()
        custo = custo_aqusicao(valor_unitario)
        tipo_compra = tipo_compra_aleatoria()
        canal_venda = tipo_pagamento_aleatorio()
        regiao = random.choice(regioes)

        registro = [data, produto, categoria_produto, quantidade, tipo,
                    valor_unitario, custo, tipo_compra, canal_venda, regiao]

        print("\tRegistro %d: %s." % (i + 1, registro))

        # Escreve a linha no arquivo CSV
        arquivo.writerow(registro)


# Abre o arquivo gerado
df = pd.read_csv(r''+caminho_base_dados, encoding='utf-8')

# Converte a data para o formato pandas.datetime
df['Data'] = pd.to_datetime(df['Data'])

# Ordena a coluna de acordo com o atributo 'Data' e refaz o indice
df = df.sort_values(['Data'], ignore_index=True)

# Salva o arquivo após tratamento
df.to_csv(r''+caminho_base_dados, index=False, encoding='utf-8')

print("Processo finalizado com sucesso!")
