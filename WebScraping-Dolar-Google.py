import requests
from bs4 import BeautifulSoup


link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, 'html.parser')

print("Pesquisa realizada: ", site.find('textarea', class_='gLFyf')['value'])
print("Valor: ", site.find('span', class_='DFlfde SwHCTb')['data-value'])
