# Compra e Venda de Produtos
Este projeto foi desenvolvido com o intuito de criar uma base de dados aleatória relacionada a compra e venda de produtos. O objetivo de tal base de dados é servir como um modelo para realizar as análises dos dados posteriormente por intermédio de recursos analiticos e criação de *dashboards*

Para a criação desta base de dados foi redigido o código `criar.py`, responsável por coletar as informações e gerar aleatoriamente os dados, de acordo com os parâmetros.

---
## O arquivo ``lista_produtos.json``
O arquivo JSON ``lista_produtos.json`` é utilizado para criar a variação de produtos e suas respectivas categorias. Este arquivo é do tipo *Array of Object* onde, o primeiro campo refere-se ao produto e o segundo, a categoria deste.

Abaixo, temos um exemplo de arquivo JSON utilizado.

```js
[
    {
        "Produto": "Notebook Dell",
        "Categoria": "Notebook"
    },
    {
        "Produto": "Monitor Asus ROG",
        "Categoria": "Monitor"
    },
    {
        "Produto": "Teclado Logitech",
        "Categoria": "Periférico"
    },
    {
        "Produto": "Impressora Brother",
        "Categoria": "Impressora"
    }
]
```

---

## O arquivo ``municipios_uf_brasil.csv``
O arquivo `municipios_uf_brasil.csv` possui todos os **Municipios brasileiros** e suas respectivas **Unidades Federativas**. Estes dados foram obtidos através do portal `gov.br` de forma pública.

---

## A base de dados ``base_dados.csv``
A base de dados aleatória possui os seguintes atributos:

1. **`Data`**: Atributo aleatório do tipo `pandas.datetime`. A data varia entre o dia **01/01/2010** até o dia **31/12/2023** em dias úteis e o horário das **9h** às **17h**. O valor é gerado na função `rd_data()` e utiliza as informações das variáveis abaixo:
   * A **data inicial** pode ser modificada alterando o valor da variável ``data_inicial`` no arquivo ``criar.py``.
   * A **data final** pode ser modificada alterando o valor da variável ``data_final`` no arquivo ``criar.py``.
   * A **hora inicial** pode ser modificada alterando o valor da variável ``hora_inicial`` no arquivo ``criar.py``.
   * A **hora final** pode ser modificada alterando o valor da vairável ``hora_final`` no arquivo ``criar.py``.

2. **`Produto`**: Atributo aleatório do tipo `pandas.object`. Este campo pode variar de acordo com os produtos lançados no arquivo `lista_produtos.json`. Este arquivo **JSON** segue o padrão *Array of Object*, sem um indice. É possível visualizar o processo na função `rd_produto()`.

3. `Categoria`: Atributo aleatório do tipo `pandas.object`. É um subgrupo do atributo `Produto`, carregado do arquivo **JSON**.

4. **`Quantidade`**: Atributo aleatório do tipo `pandas.object`. Gera uma quantidade aleatória entre os valores **1** e **100**, em unidades. A quantidade máxima de produtos pode ser alterada na variável ``qtd_maxima`` dentro da função ``rd_quantidade``.

5. **`Tipo`**: Atributo aleatório do tipo `pandas.object` que varia entre **Compra** e **Venda**.

6. **`Valor Unitário`**: Atributo aleatório do tipo `pandas.float64` que varia de 100 a 5000.

7. **`Custo de Aquisição`**: Atributo aleatório do tipo `pandas.float64`. O custo varia entre **30%** e **70%** do `Valor Unitário`.

8. **`Canal de Venda`**: Atributo do tipo `pandas.object` que varia entre **Online**, **Loja Física**, e **Distribuidor**. Está definido no função `rd_canal()`.

9. **`Método de Pagamento`**: Atributo aleatório do tipo `pandas.object`. Varia entre **Cartão de Crédito**, **A Vista**, **Boleto** ou **Transferência Bancária**. Estes valores estão definidos no função `rd_pagamento()`.

10. **`Estado`**: Atributo aleatório do tipo `pandas.object`. Representa uma das Unidades Federativas do Brasil. Esta informação é obtida por intermédio do arquivo `municipios_uf_brasil.csv`.

11. **`Municipio`**: Atributo aleatório do tipo `pandas.object`. Representa um municipio brasileiro, de acordo com o atributo `Estado`. Esta informação é obtida por intermédio do arquivo `municipios_uf_brasil.csv`.

O arquivo será salvo em ordem cronológica com o nome atribuido, no formato CSV em UTF-8. Como teste, gerei uma base de dados com 1.000.000 de registros com um tamanho de 106MB.