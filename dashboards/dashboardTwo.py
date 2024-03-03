import streamlit as st
import pandas as pd
import numpy as np

# Configuração inicial da página
st.set_page_config(page_title="Relação Preço e Taxa", page_icon="⚖️", layout='wide')

# Para usar estilo CSS
with open(r'dashboards\styleTwo.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Criação dos dados
df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['Preço','Taxa de ocupação','Taxa de inadimplência']
)

st.sidebar.image(r'dashboards\logo.png', use_column_width=True)
st.sidebar.header("Dashboard")
st.sidebar.caption("Clique no botão para exibir o gráfico.")

if st.sidebar.button("Exibir Gráfico"):
    st.header("Meu Gráfico")
    df = pd.DataFrame(
        np.random.rand(10, 3),
        columns = ['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência']
    )
    
    st.bar_chart(df, color=["#003469","#008037","#99CCAF"])
    st.area_chart(df)
    #st.sidebar.code(df)
