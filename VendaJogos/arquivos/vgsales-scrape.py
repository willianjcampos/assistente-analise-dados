from bs4 import BeautifulSoup, element
import urllib.request
import pandas as pd
import numpy as np
import re
import time

from datetime import datetime

pages = 1299 # Quantidade de páginas no site. Esta informação foi verificada no site e informado manualmente
rec_count = 6051

# URL Base
urlhead = 'https://www.vgchartz.com/games/games.php?page='

# Filtros de Seleção para exibição da lista
urltail = '&results=50'  # Quantidade de dados exibida por página, padrão 50. Com a quantidade de 200, serão 325 páginas.
urltail += '&order=Game' # Classificação da lista
urltail += '&ownership=Both' # Proprietário (todos)
urltail += '&direction=ASC' # Listar de forma ascendente
urltail += '&showtotalsales=1'  # Exibe a lista com o valor total de vendas (sales_gl)
urltail += '&shownasales=1'  # Exibe a lista com o valor de venda NA (sales_na)
urltail += '&showpalsales=1'  # Exibe a lista com o valor de venda PAL (sales_pal)
urltail += '&showjapansales=1'  # Exibe a lista com o valor de venda JP (sales_jp)
urltail += '&showothersales=1'  # Exibe a lista com o valor de venda em outros locais (sales_ot)
urltail += '&showpublisher=1'  # Exibir a distribuidora do jogo eletrônico (publisher)
urltail += '&showdeveloper=1'  # Exibe o nome do desenvolvedor do jogo eletrônico (developer)
urltail += '&showreleasedate=1'  # Exibe a informação de lançamento do jogo (day, month e year)
urltail += '&showlastupdate=0'  # Exibe a informação de ultima atualização (não está sendo usado)
urltail += '&showvgchartzscore=0'  # Exibe a informação relacionada a nota do proprio site (não está sendo usado)
urltail += '&showcriticscore=1'  # Exibe a pontuação do jogo de acordo com as criticas (critic_score)
urltail += '&showuserscore=1'  # Exibe a pontuação do jogo de acordo com as criticas dos usuários (user_score)
urltail += '&showshipped=0'  # Exibe a quantidade estimada de envios (não está sendo usado)

for page in range(122, pages):
    # Cria as variaveis
    rank = []
    gname = []
    platform = []
    day = []
    month = []
    year = []
    genre = []
    critic_score = []
    user_score = []
    publisher = []
    developer = []
    sales_na = []
    sales_pal = []
    sales_jp = []
    sales_ot = []
    sales_gl = []

    surl = urlhead + str(page) + urltail
    r = urllib.request.urlopen(surl).read()
    soup = BeautifulSoup(r, features='lxml')

    print(f"Página: {page} de {pages}: {surl}")

    game_tags = list(soup.find_all('a', href=re.compile('https://www.vgchartz.com/game/')))

    for tag in game_tags:  # Vai percorrer a lista da primeira página 50x por página (aproximados)
        # Adiciona o nome do jogo na lista
        gname.append(" ".join(tag.string.split()))
        print(f"{rec_count} Jogo encontrado. Buscando dados para {gname[-1]}")

        # Refaz a leitura e capta uma outra sub tag
        data = tag.parent.parent.find_all("td")
        
        rank.append(np.int32(data[0].string)) # ID ou Rank de acordo com a lista
        
        platform.append(data[3].find('img').attrs['alt'].strip())  # Procura a imagem que representa a Plataforma e captura a informação da tag 'alt'
        
        publisher.append(data[4].string.strip() if
                         not data[4].string.startswith("Unknown") else np.nan)  # Existem informações que são desconhecidas. Fazer um scrape na wikipedia para obter a informação pode ser uma via interessante... Caso não haja informação, será substituido 'Unknow' por un np.nan
        
        developer.append(data[5].string.strip())

        critic_score.append(
            float(data[6].string) if
            not data[6].string.startswith("N/A") else np.nan)
        
        user_score.append(
            float(data[7].string) if
            not data[7].string.startswith("N/A") else np.nan)
        
        sales_gl.append(
            float(data[8].string[:-1]) if
            not data[8].string.startswith("N/A") else np.nan)

        sales_na.append(
            float(data[9].string[:-1]) if
            not data[9].string.startswith("N/A") else np.nan)
        
        sales_pal.append(
            float(data[10].string[:-1]) if
            not data[10].string.startswith("N/A") else np.nan)
        
        sales_jp.append(
            float(data[11].string[:-1]) if
            not data[11].string.startswith("N/A") else np.nan)
        
        sales_ot.append(
            float(data[12].string[:-1]) if
            not data[12].string.startswith("N/A") else np.nan)
        
        # Lançamento
        release_year = data[13].string.split()[-1]
        if release_year.startswith('N/A'):
            year.append(np.nan)
            month.append(np.nan)
            day.append(np.nan)
        else:
            # Tratamento Ano
            if int(release_year) >= 80:
                year_to_add = np.int32("19" + release_year)
            else:
                year_to_add = np.int32("20" + release_year)
            year.append(year_to_add)

            # Tratamento Mês
            release_month = data[13].string.split()[-2]
            month.append(datetime.strptime(release_month, '%b').month)  # Realiza a conversão para INT

            # Tratamento Dia
            release_day = data[13].string.split()[-3]
            day.append(int(release_day.strip()[:-2]))


        # Acessa a pagina individual de cada jogo
        url_to_game = tag.attrs['href']
        site_raw = urllib.request.urlopen(url_to_game).read()
        sub_soup = BeautifulSoup(site_raw, "html.parser")

        
        # Localiza a div com o box que possui a informação do gênero
        # No código, existem 2 H2, um com a informação de 'Developer' e a outra com 'Genre'
        h2s = sub_soup.find("div", {"id": "gameGenInfoBox"}).find_all('h2')

        # Cria uma tag temporaria para buscar a informação desejada
        temp_tag = element.Tag
        for h2 in h2s:
            if h2.string == 'Genre':
                temp_tag = h2
        genre.append(temp_tag.next_sibling.string)

        rec_count += 1

    columns = {
        'Rank': rank,
        'Name': gname,
        'Platform': platform,
        'Day': day,
        'Month': month,
        'Year': year,
        'Genre': genre,
        'Publisher': publisher,
        'Developer': developer,
        'Critic_Score': critic_score,
        'User_Score': user_score,
        'NA_Sales': sales_na,
        'PAL_Sales': sales_pal,
        'JP_Sales': sales_jp,
        'Other_Sales': sales_ot,
        'Global_Sales': sales_gl
    }

    print("\nCriando DataFrame...")
    df = pd.DataFrame(columns)

    df = df[[
        'Rank', 'Name', 'Platform', 'Day', 'Month', 'Year', 'Genre',
        'Publisher', 'Developer', 'Critic_Score', 'User_Score',
        'NA_Sales', 'PAL_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]

    print("Salvando informações no arquivo...")
    arquivo_part = f'VendaJogos/arquivos/vgsales/vgsales-scrape{page}.csv'
    df.to_csv(arquivo_part, sep=',', encoding='utf-8', index=False)

    # Limpeza de cache
    print("Limpeza de cache de Memória...")
    del rank
    del gname
    del platform
    del day
    del month
    del year
    del genre
    del publisher
    del developer
    del critic_score
    del user_score
    del sales_na
    del sales_pal
    del sales_jp
    del sales_ot
    del sales_gl

    print("Aguardando time de 10 segundos para iniciar a próxima página")
    time.sleep(10)  # Espera 10 segundos antes de passar para a próxima página

    print("\n\n")
