-- Script para criar o modelo relacional normalizado, já com os relacionamentos corretos.
CREATE TABLE Cliente (
  idCliente INTEGER NOT NULL PRIMARY KEY,
  nomeCliente VARCHAR(255) NOT NULL,
  cidadeCliente VARCHAR(255),
  estadoCliente VARCHAR(255),
  paisCliente VARCHAR(255)
);

CREATE TABLE Carro (
  idCarro INTEGER NOT NULL PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro VARCHAR(255),
  marcaCarro VARCHAR(255),
  modeloCarro VARCHAR(255),
  anoCarro INTEGER,
  idcombustivel INTEGER NOT NULL,
  tipoCombustivel VARCHAR(255),
  FOREIGN KEY (idcombustivel) REFERENCES Combustivel (idcombustivel)
);

CREATE TABLE Locacao (
  idLocacao INTEGER NOT NULL PRIMARY KEY,
  idCliente INTEGER NOT NULL,
  idCarro INTEGER NOT NULL,
  qtdDiaria INTEGER,
  vlrDiaria DECIMAL,
  dataLocacao DATE,
  horaLocacao TIME,
  idVendedor INTEGER,
  FOREIGN KEY (idCliente) REFERENCES Cliente (idCliente),
  FOREIGN KEY (idCarro) REFERENCES Carro (idCarro),
  FOREIGN KEY (idVendedor) REFERENCES Vendedor (idVendedor)
);

CREATE TABLE Combustivel (
  idcombustivel INTEGER NOT NULL PRIMARY KEY,
  tipoCombustivel VARCHAR(255)
);

CREATE TABLE Vendedor (
  idVendedor INTEGER NOT NULL PRIMARY KEY,
  nomeVendedor VARCHAR(255),
  sexoVendedor SMALLINT(1),
  estadoVendedor VARCHAR(255)
);

-- Spript para colocar os dados da tabela "desnormalizada" nesse modelo relacional normalizado.
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idLocacao, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel)
SELECT idLocacao, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCarro, tipoCombustivel
FROM tb_locacao;

INSERT INTO Locacao (idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, idVendedor)
SELECT idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, idVendedor
FROM tb_locacao;

-- o OR IGNORE é para ignorar os dados duplicados no INSERT
INSERT OR IGNORE INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT idcombustivel, tipoCombustivel
FROM tb_locacao;

INSERT OR IGNORE INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;
