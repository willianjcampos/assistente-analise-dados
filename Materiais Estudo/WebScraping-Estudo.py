import response
import requests
from bs4 import BeautifulSoup


link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+do+dolar"
requisicao = requests.get(link)
# Neste Momento, exibe o código do response (resposta do servidor)
#print(requisicao)

# Exibe a página no formato HTML
#print(requisicao.text)

# Melhora a visualização do HTML
site = BeautifulSoup(requisicao.text, 'html.parser')
# Exibe o código do site de maneira mais visivel
#print(site.prettify())

# Exibe o título do site
#print("Titulo: ", site.title)

# Uma forma de buscar o titulo (tag), por exemplo, seria usando o comando 'find'
#print("Titulo, 2nd Opção: ", site.find('title'))

# Pesquisa todos as tags do tipo input
#print("Input: ", site.find_all('input'))

# Pesquisa uma tag do tipo input com name = 'q'
# Ele retorna um erro devido a bloqueios no site
#print("Input 2: ", site.find('input', name='q'))

# Pesquisa uma tag do tipo textarea com class = 'gLFyf' (pesquisa)
# Ele retorna none devido a bloqueios no site, que identifica a busca por Python
#print("Input 2: ", site.find('textarea', class_='gLFyf'))

# Para contornar isso, basta informar que a requisição foi realizada por um navegador
# Para isso, informe os headers (Inspecionar -> Network -> Request Headers -> User Agents)
# Por essa razão, cria-se uma variável do tipo dicionário seguindo a forma abaixo e passa no 'requests'
# Aqui, por questões de documentação, repeti o código anterior
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, 'html.parser')

# Pesquisa uma tag do tipo textarea com class = 'gLFyf' (pesquisa)
# Com as modificações realizadas, ele passa a retornar o valor corretamente
#print("Campo de Pesquisa: ", site.find('textarea', class_='gLFyf'))

# Filtra apenas o valor ('value') da pesquisa realizada
print("Pesquisa realizada: ", site.find('textarea', class_='gLFyf')['value'])
