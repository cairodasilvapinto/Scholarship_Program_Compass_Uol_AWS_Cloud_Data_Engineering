Um banco de dados dimensional é uma estrutura de banco de dados otimizada para Data Warehousing e Business Intelligence. Ele é composto por “fatos” e “dimensões”. Fatos são métricas numéricas baseadas em eventos de negócios, enquanto dimensões são as categorias pelas quais os fatos são divididos para análise.

No banco de dados dimensional criado:

1. DimCliente, DimCarro, DimVendedor: Estas são as tabelas de dimensão. Elas contêm os atributos que você deseja analisar os fatos. Por exemplo, você pode querer analisar as vendas (um fato) por cliente, carro ou vendedor (dimensões).

2. FatoLocacao: Esta é a tabela de fatos. Ela contém as métricas numéricas (neste caso, qtdDiaria e vlrDiaria) que você deseja analisar. A tabela de fatos também contém chaves estrangeiras para as tabelas de dimensão, permitindo que você divida os fatos por qualquer combinação de dimensões.

3. Chaves estrangeiras nas tabelas de fatos: As chaves estrangeiras na tabela de fatos (idCliente, idCarro, idVendedor) referenciam as chaves primárias nas tabelas de dimensão. Isso permite que você junte as tabelas de fatos e dimensões para analisar os fatos divididos por dimensões.