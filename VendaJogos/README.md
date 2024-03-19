# Projeto de Análise de DataFrame

Este projeto foi criado para efetuar a avaliação relacionada ao desenvolvimento de Dashboards através de ferramentas de exibição gráfica em conjunto com o Streamlit para gerar relatórios em formato Web dinâmicos.


## Sobre o Projeto
1. No diretório `arquivos` encontram-se alguns arquivos utilizando durante a execução deste projeto:
   * `vgsales-analise.ipynb`: Arquivo criado com o intuito de analisar as informações da base de dados `vgsales.csv` e, posteriormente, o arquivo `vgsales-scrape.csv` oriundo do processo de scrape.
   * `vgsales-bd-tratado.csv`: Arquivo gerado através da execução do arquivo `vgsales-analise.ipynb`, sendo o resultado do processo de limpeza e adequação da base de dados.
   * `vgsales-scrape.py`: Arquivo python com o processo de Scrape adaptado da fonte que gerou o banco de dados. Foi utilizado para realizar o processo de coleta das informações de forma atualizada.
   * `vgsales.csv`: Arquivo baixado do Kaggle utilizado para analise preliminar das informações. Depois deste processo, foi realizado o processo de scrape na fonte da base de dados para atualizar as informações.
   * `vgsales-scrape.csv`: Arquivo resultante do processo de scrape realizado através da execução do arquivo `vgsales-scrape.py`, originalmente desenvolvido pelo usuário [GregorUT](https://github.com/GregorUT/vgchartzScrape), adaptado e atualizado para obter as informações recentes da página [VGChartz](https://www.vgchartz.com/).

0. O projeto do Streamlit é executado através do arquivo `app.py`, encontrado no diretório raiz do projeto.

0. No digetório `pg` encontram-se as páginas utilizada para a paginação e organização do projeto do Streamlit.

0. Com o intuito de separar algumas configurações, parte dos estilos encontram-se no arquivo `vgsales-syle.css`, importado no arquivo `app.py`. Existem algumas configurações de estilo que só foram possíveis de serem executadas dentro do prórpio arquivo *(ainda não encontrei um meio de separar todos os estilos e centrar em um único arquivo)*.
