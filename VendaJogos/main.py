import streamlit as st
from streamlit_option_menu import option_menu
import pg.home as home, pg.analitico as analitico, pg.estrategico as estrategico, pg.tatico as tatico, pg.outros as outros, pg.informacoes as informacoes
import pandas as pd



## Configuração da Página
st.set_page_config(
    page_title="Venda de Jogos",
    page_icon="⚖️",
    layout='wide'
)


## Para usar estilo CSS
with open(r'VendaJogos/vgsales-style.css', encoding='utf8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


## Classe Principal
@st.cache_data
class MultiApp:
    def __init__(self) -> None:
        self.app = []


    def run():
        # Carrega a base de dados
        df = pd.read_csv(r'VendaJogos/vgsales-bd-tratado.csv', encoding='utf-8')


        # Configura Sidebar
        with st.sidebar:
            # Configuração do Menu
            app = option_menu(
                menu_title="Venda de Jogos",
                options=['Home', 'Tático', 'Estratégico', 'Analítico', 'Outros', 'Informações'],
                icons=[],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    'container': {'padding': '5px !important'},
                    'icon': {'font-size': '14px'},
                    'nav-link': {'font-size': '14px',
                                 'text-align': 'left',
                                 'margin': '2px 0px',
                                 '--bs-nav-link-padding-x': '0.5rem',
                                 '--bs-nav-link-padding-y': '0.5rem'},
                    'nav-link-selected': {'font-size': '14px',
                                          'font-weight': 'normal'}
                }
            )
            anos = sorted(df['Year'].unique())
            anos_selecionados = st.multiselect('Anos:', anos, placeholder='Selecione...')

            genero = sorted(df['Genre'].unique())
            genero_selecionados = st.multiselect('Gênero:', genero, placeholder='Selecione...')

            desenvolvedora = sorted(df['Publisher'].unique())
            desenvolvedora_selecionados = st.multiselect('Desenvolvedora:', desenvolvedora, placeholder='Selecione...')

        if app == 'Home':
            home.app(df, anos_selecionados, genero_selecionados, desenvolvedora_selecionados)
        
        if app == 'Analítico':
            analitico.app()

        if app == 'Estratégico':
            estrategico.app()

        if app == 'Tático':
            tatico.app()
        
        if app == 'Outros':
            outros.app(df)
            
        if app == 'Informações':
            informacoes.app()
    

    run()
