import streamlit as st


def app():
    st.write(
        """
        OUTRAS ANÁLISES PARA FAZER:\n
            1. Melhores Plataformas por região (NA, EU, JP, Global, Outros);
            2. Foi identificado que, na coluna 'Global', o valor está passando 0.09 da soma dos locais;
            
        """,
        unsafe_allow_html=True
    )