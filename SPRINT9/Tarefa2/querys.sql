-- Criando as Tabelas
-- Dimensão Cliente
CREATE TABLE DimCliente (
  idCliente INTEGER NOT NULL PRIMARY KEY,
  nomeCliente VARCHAR(255) NOT NULL,
  cidadeCliente VARCHAR(255),
  estadoCliente VARCHAR(255),
  paisCliente VARCHAR(255)
);

-- Dimensão Carro
CREATE TABLE DimCarro (
  idCarro INTEGER NOT NULL PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro VARCHAR(255),
  marcaCarro VARCHAR(255),
  modeloCarro VARCHAR(255),
  anoCarro INTEGER,
  tipoCombustivel VARCHAR(255)
);

-- Dimensão Vendedor
CREATE TABLE DimVendedor (
  idVendedor INTEGER NOT NULL PRIMARY KEY,
  nomeVendedor VARCHAR(255),
  sexoVendedor SMALLINT(1),
  estadoVendedor VARCHAR(255)
);

-- Fato Locação
CREATE TABLE FatoLocacao (
  idLocacao INTEGER NOT NULL PRIMARY KEY,
  idCliente INTEGER NOT NULL,
  idCarro INTEGER NOT NULL,
  qtdDiaria INTEGER,
  vlrDiaria DECIMAL,
  dataLocacao DATE,
  horaLocacao TIME,
  idVendedor INTEGER,
  FOREIGN KEY (idCliente) REFERENCES DimCliente (idCliente),
  FOREIGN KEY (idCarro) REFERENCES DimCarro (idCarro),
  FOREIGN KEY (idVendedor) REFERENCES DimVendedor (idVendedor)
);

-- Criando as Views
-- Dimensão Cliente
CREATE VIEW vwCliente AS
SELECT
  idCliente,
  nomeCliente,	
  cidadeCliente,
  estadoCliente,
  paisCliente
FROM Cliente;

-- Dimensão Carro
CREATE VIEW vwCarro AS
SELECT
  idCarro,
  kmCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  tipoCombustivel
FROM Carro;

-- Dimensão Vendedor
CREATE VIEW vwVendedor AS
SELECT
  idVendedor,
  nomeVendedor,
  sexoVendedor,
  estadoVendedor
FROM Vendedor;

-- Fato Locação
CREATE VIEW vwLocacao AS
SELECT
  idLocacao,
  idCliente,
  idCarro,
  qtdDiaria,
  vlrDiaria,
  dataLocacao,
  horaLocacao
FROM Locacao;

-- Eu inseri os dados das tabelas relacionais normalizadas aqui para fazer testes de consulta.
-- Inserir dados na tabela DimCliente
INSERT INTO DimCliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente FROM Cliente;

-- Inserir dados na tabela DimCarro
INSERT INTO DimCarro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel FROM Carro;

-- Inserir dados na tabela DimVendedor
INSERT INTO DimVendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM Vendedor;

-- Inserir dados na tabela FatoLocacao
INSERT INTO FatoLocacao (idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, idVendedor)
SELECT idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, idVendedor FROM Locacao;

--Consulta para ver total de vendas do vendedor:
SELECT 
  v.idVendedor,
  v.nomeVendedor,
  SUM(l.vlrDiaria * l.qtdDiaria) AS totalVendas
FROM 
  FatoLocacao l
JOIN 
  DimVendedor v ON l.idVendedor = v.idVendedor
GROUP BY 
  v.idVendedor, v.nomeVendedor;

idVendedor|nomeVendedor           |totalVendas|
----------+-----------------------+-----------+
         5|Vendedor cinco         |        400|
         6|Vendedora seis         |       6350|
         7|Vendedora sete         |        750|
         8|Vendedora oito         |       5000|
        16|Vendedor dezesseis     |      20100|
        30|Vendedor trinta        |      12000|
        31|Vendedor trinta e um   |       9000|
        32|Vendedora trinta e dois|      12600|

-- Consulta para ver carros mais populares entre os clientes:
SELECT 
  c.idCarro,
  c.marcaCarro,
  c.modeloCarro,
  COUNT(l.idLocacao) AS totalLocacoes
FROM 
  FatoLocacao l
JOIN 
  DimCarro c ON l.idCarro = c.idCarro
GROUP BY 
  c.idCarro, c.marcaCarro, c.modeloCarro
ORDER BY 
  totalLocacoes DESC;

idCarro|marcaCarro|modeloCarro|totalLocacoes|
-------+----------+-----------+-------------+
      5|Fiat      |Fiat Palio |            5|
      2|Fiat      |Fiat Uno   |            4|
      3|Fiat      |Fiat Palio |            4|
      4|Fiat      |Fiat Palio |            3|
      1|Fiat      |Fiat Uno   |            2|
      6|VW        |Fusca 78   |            1|
      7|VW        |Fusca 78   |            1|
     10|Fiat      |Fiat 147   |            1|