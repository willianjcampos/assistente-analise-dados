# Criado dia 15/02/2024

import pandas as pd

# Criando um DataFrame de exemplo
data = {'Nome': ['João', 'Ana', 'Carlos', 'Maria', 'Pedro'],
        'Idade': [23, 78, 22, 19, 45],
        'Cidade': ['Belo Horizonte', 'Fortaleza', 'Brasília', 'São Paulo', 'Rio de Janeiro']}

df = pd.DataFrame(data)

# Filtrando pessoas com mais de 25 anos
df_filtrado = df[df['Idade'] > 25]

print("Dados sem Filtragem")
print(df)

print("\nDados Filtrados")
print(df_filtrado)
