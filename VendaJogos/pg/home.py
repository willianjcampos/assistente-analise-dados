import streamlit as st
import pandas as pd
import locale
import altair as alt
import streamlit.components.v1 as components

bloco_estilo = '''
                        <style>
                            *{
                                margin: 0px;
                                padding: 0px;
                            }
                            body{
                                background-color: #FF4B4B;
                                padding: .5rem;
                                color: #FFFFFF;
                                font-family: sans-serif;
                            }
                            body:hover{
                                cursor: pointer;
                            }
                            h1, p{
                                text-align: center;
                                font-size: 18px;
                                padding: .3rem 0rem;
                            }
                        </style>
                    '''


def cols_primeira_linha(df):
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

    col1, col2, col3, col4, col5 = st.columns(5)

    

    with col1:
        ns_sales_total = locale.format('%.2f', df['NA_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>NA</h1>
                <p>{ns_sales_total}</p>
            """
        )
        

    with col2:
       eu_sales_total = locale.format('%.2f', df['EU_Sales'].sum(), True)

       components.html(
            f"""
                {bloco_estilo}
                <h1>EU</h1>
                <p>{eu_sales_total}</p>
            """
        )
       
    with col3:
        jp_sales_total = locale.format('%.2f', df['JP_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>JP</h1>
                <p>{jp_sales_total}</p>
            """
        )

    with col4:
        other_sales_total = locale.format('%.2f', df['Other_Sales'].sum(), True)

        components.html(
            f"""
                {bloco_estilo}
                <h1>OUTROS</h1>
                <p>{other_sales_total}</p>
            """
        )

    with col5:
        global_sales_total = locale.format('%.2f', df['Global_Sales'].sum(), True)

        components.html(
            f"""
                <body style='background-color: blue;'>
                {bloco_estilo}
                <h1>TOTAL</h1>
                <p>{global_sales_total}</p>
                </body>
            """
        )



def cols_segunda_linha(eixo_x, eixo_y, df_genero):
    col1, col2 = st.columns([3, 2])

    # Gráfico de Linhas
    with col1:
        grafico3 = pd.DataFrame({'Volume de Vendas de Jogos': eixo_y,
                        'Anos': eixo_x})

        st.write(alt.Chart(grafico3,
                        title=alt.Title(
                            "Venda de Jogos",
                            subtitle="Volume de vendas de Jogos ao longo dos anos"
                            ),
                            width="container"
                            ).mark_line(point=True,
                                        color='#FF4B4B',
                                        interpolate='cardinal'
                                        ).encode(x=alt.X('Anos', sort=None),
                                                y='Volume de Vendas de Jogos',
                                                ).interactive())

    # Gráfico de Pizza
    with col2:
        x4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(ascending=False).index # Nomes (names)
        y4 = df_genero.groupby(['Genre'])['Genre'].count().sort_values(ascending=False) # Quantidade (values)

        grafico4 = pd.DataFrame({'Setores': x4,
                    'Valores': y4})


        st.write(alt.Chart(grafico4,
                        title=alt.Title(
                            "Venda de Jogos por Gênero",
                            subtitle="Volume de vendas por Gênero"
                            ),
                            width='container'
                        ).mark_arc(innerRadius=70).encode(
            theta='Valores',
            color='Setores',
        ).interactive())



def cols_terceira_linha(eixo_x, eixo_y):
    col1, col2 = st.columns([1, 5])
    
    # Rank
    with col1:
        contagem = 3
        if len(eixo_x) >= contagem:
            for i in range(contagem):
                p = i + 1
                titulo = str('%iº' %p)
                valor = str(eixo_x[i] + " - " + locale.format('%d', eixo_y[i], True))
                components.html(f"""
                                {bloco_estilo}
                                <h1>{titulo}</h1>
                                <p>{valor}</p>
                                """)
                
                

        elif len(eixo_x) >= 1:
            #st.header('1º')
            #st.write(eixo_x[0] + " - " + locale.format('%d', eixo_y[0], True))
            titulo = "1º"
            valor = str(eixo_x[0] + " - " + locale.format('%d', eixo_y[0], True))
            components.html(f"""
                                {bloco_estilo}
                                <h1>{titulo}</h1>
                                <p>{valor}</p>
                                """)

        else:
            st.write('Dados indisponíveis')

        

    # Gráfico de Barras
    with col2:
        grafico = pd.DataFrame({'Plataformas': eixo_x[0:10],
                    'Quantidade': eixo_y[0:10]})

        st.write(alt.Chart(grafico,
                        title=alt.Title(
                            "Plataformas",
                            subtitle="As 10 Plataformas que mais reuniram recursos"
                            ),
                            width="container"
                        ).mark_bar(color='#FF4B4B').encode(
            x=alt.X('Plataformas', sort=None),
            y='Quantidade'
        ).interactive())



    


def app(df, anos_selecionados, genero_selecionados, desenvolvedora_selecionados):
    # Cria as variáveis de filtros
    df_ano = df[df['Year'].isin(anos_selecionados)]
    df_genero = df[df['Genre'].isin(genero_selecionados)]
    df_desenvolvedora = df[df['Genre'].isin(desenvolvedora_selecionados)]

    if df_ano.shape[0] > 0:
        if df_genero.shape[0] > 0:
            if df_desenvolvedora.shape[0] > 0:
                df_analise = df[(df_ano & df_genero & df_desenvolvedora)]

    ## PRIMEIRA LINHA
    # Verifica Filtro de Período (Anos) de Venda
    if df_ano.shape[0] > 0:
        cols_primeira_linha(df_ano)
        
    else:
        cols_primeira_linha(df)
    
    
    # SEGUNDA LINHA
    # Verifica Filtro de Gênero de Jogos
    if df_genero.shape[0] > 0:
        eixo_x = df_genero.groupby(['Year'])['Year'].count().index
        eixo_y = df_genero.groupby(['Year'])['Year'].count()
        cols_segunda_linha(eixo_x, eixo_y, df_genero)

    else:
        eixo_x = df.groupby(['Year'])['Year'].count().index
        eixo_y = df.groupby(['Year'])['Year'].count()
        cols_segunda_linha(eixo_x, eixo_y, df)
    
    
    
    
    ## TERCEIRA LINHA
    if df_genero.shape[0] > 0:
        eixo_x = df_genero.groupby(['Platform'])['Platform'].count().sort_values(ascending=False).index
        eixo_y = df_genero.groupby(['Platform'])['Platform'].count().sort_values(ascending=False)

    else:
        eixo_x = df.groupby(['Platform'])['Platform'].count().sort_values(ascending=False).index
        eixo_y = df.groupby(['Platform'])['Platform'].count().sort_values(ascending=False)

    cols_terceira_linha(eixo_x, eixo_y)
    
    
