# Compra e Venda de Produtos de Informática

Este projeto foi desenvolvido com o intuito de criar uma base de dados aleatória relacionada a compra e venda de produtos da área de informática. O objetivo de tal base de dados é servir como um modelo para realizar as análises dos dados posteriormente através de estudos dos campos.

---
## O arquivo JSON
O arquivo JSON é utilizado para subir no python os produtos e sua respectiva categoria. Este arquivo é do tipo *Array of Object*, onde, o primeiro campo refere-se ao produto e o segundo, a categoria.

Segue abaixo o padrão utilizado com dados de exemplo.

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

## A Base de Dados Criada

A base de dados aleatória possui os seguintes atributos:
1. `Data`: Atributo aleatório do tipo `pandas.datetime`. A data varia entre o dia **01/01/2010** até o dia **31/12/2023** em dias úteis e o horário das **9h** às **17h**.
2. `Produto`: Atributo aleatório do tipo `pandas.object`. Este campo pode variar de acordo com os produtos lançados no arquivo `lista_produtos.json`. Este arquivo **JSON** segue o padrão *Array of Object*, sem um indice.
3. `Categoria`: Atributo aleatório do tipo `pandas.object`. É um subgrupo do atributo `Produto`, carregado do arquivo **JSON**.
4. `Quantidade`: Atributo aleatório do tipo `pandas.object`. Gera uma quantidade aleatória entre os valores **1** e **100**, em unidades.
5. `Tipo`: Varia entre **Compra** e **Venda**.
6. `Valor Unitário`: Atributo aleatório do tipo `pandas.float64` que varia de 100 a 5000.
7. `Custo de Aquisição`: Atributo aleatório do tipo `pandas.float64`. O custo varia entre **30%** e **70%** do `Valor Unitário`.
8. `Canal de Venda`: Atributo do tipo `pandas.object` que varia entre **Online**, **Loja Física**, e **Distribuidor**. Está definido no função `canal_venda_aleatorio()`.
9. `Método de Pagamento`: Atributo aleatório do tipo `pandas.object`. Varia entre **Cartão de Crédito**, **Boleto**, **Transferência Bancária**. Estes valores estão definidos no função `tipo_pagamento_aleatorio()`.
10. `Região`: Atributo aleatório do tipo `pandas.object`. Representa uma região onde o produto pode ser vendido. Por padrão, possuimos os estados de **Goiás**, **Minas Gerais** e **Mato Grosso**. Estes valores estão definidos no função `regiao_aleatoria()`.


O arquivo será salvo em ordem cronológica com o nome atribuido, no formato CSV em UTF-8. Como teste, gerei uma base de dados com 1.000.000 de registros com um tamanho de 106MB.