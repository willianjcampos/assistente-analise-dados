import streamlit as st
import pandas as pd
import numpy as np

# Para usar estilo CSS (metodo chato...)
#with open('styleOne.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Layout da página - Para alterar estilo
#st.markdown(page_bg_img, unsafe_allow_html=True)

# Exibição de dados básica
df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['Preço','Taxa de ocupação','Taxa de inadimplência']
)

# Configurações da Página - No tema padrão
st.set_page_config(page_title="Relação Preço e Taxa", page_icon="⚖️", layout="wide")

# Funcionalidades de exibição
st.header("📊 Análise Preço x Taxa")

# Título
st.title("🦐 Tabela de demonstrativa básica")

# Básica
st.table(df)

# Exibição completa
st.dataframe(df)

# Exibição gráfico de linhas
st.line_chart(df)

# Exibição gráfico de colunas
st.bar_chart(df)