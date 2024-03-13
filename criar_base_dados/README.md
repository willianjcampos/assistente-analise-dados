# Compra e Venda de Produtos de Informática
## Banco de Dados Aleatório

Este projeto foi desenvolvido com o intuito de criar uma base de dados aleatória relacionada a compra e venda de produtos da área de informática. O objetivo de tal base de dados é servir como um modelo para realizar as análises dos dados posteriormente através de estudos dos campos.

A base de dados aleatória possui os seguintes atributos:
1. ```Data```: Atributo aleatório do tipo ```pandas.datetime```. A data varia entre o dia **01/01/2010** até o dia **31/12/2023** em dias úteis e o horário das **9h** às **17h**.
2. ```Produto```: Este campo pode variar de acordo com os produtos lançados no arquivo ```lista_produtos.json```. Este arquivo JSON segue o padrão *Array of Object*, sem um indice.
3. ```Categoria```: É um subgrupo do ```Produto```.
4. ```Quantidade```: Gera uma quantidade aleatória entre os valores **1** e **100**, em unidades.
5. ```Tipo```: Varia entre **Compra** e **Venda**.
6. ```Valor Unitário```: Atributo aleatório do tipo ```float64``` que varia de 100 a 5000.
7. ```Custo de Aquisição```: O custo varia entre **30%** e **70%** do ```Valor Unitário```.
8. ```Canal de Venda```: Atributo do tipo ```object``` que varia entre **Cartão de Crédito**, **Boleto** ou **Transferência Bancária**.
9. ```Método de Pagamento```: Varia entre Cartão de Crédito, Boleto, Transferência Bancária. Estes valores estão definidos no método ```tipo_pagamento_aleatorio()```.
10. ```Região```: Representa uma região onde o produto pode ser vendido. Por padrão, possuimos os estados de Goiás, Minas Gerais e Mato Grosso. Estes valores estão definidos na variável ```regioes```.


O arquivo será salvo em ordem cronológica com o nome atribuido, no formato CSV em UTF-8. Como teste, gerei uma base de dados com 1.000.000 de registros com um tamanho de 106MB.