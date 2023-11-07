--
-- File generated with SQLiteStudio v3.4.4 on ter nov 7 17:37:28 2023
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Carro
CREATE TABLE IF NOT EXISTS Carro (
    idCarro         INTEGER       NOT NULL
                                  PRIMARY KEY,
    kmCarro         INTEGER,
    classiCarro     VARCHAR (255),
    marcaCarro      VARCHAR (255),
    modeloCarro     VARCHAR (255),
    anoCarro        INTEGER,
    idcombustivel   INTEGER       NOT NULL,
    tipoCombustivel VARCHAR (255),
    FOREIGN KEY (
        idcombustivel
    )
    REFERENCES Combustivel (idcombustivel) 
);

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      1,
                      25412,
                      'AKJHKN98JY76539',
                      'Fiat',
                      'Fiat Uno',
                      2000,
                      98,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      2,
                      29450,
                      'AKJHKN98JY76539',
                      'Fiat',
                      'Fiat Uno',
                      2000,
                      98,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      3,
                      20000,
                      'IKJHKN98JY76539',
                      'Fiat',
                      'Fiat Palio',
                      2010,
                      99,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      4,
                      21000,
                      'IKJHKN98JY76539',
                      'Fiat',
                      'Fiat Palio',
                      2010,
                      99,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      5,
                      21700,
                      'IKJHKN98JY76539',
                      'Fiat',
                      'Fiat Palio',
                      2010,
                      99,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      6,
                      121700,
                      'DKSHKNS8JS76S39',
                      'VW',
                      'Fusca 78',
                      1978,
                      3,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      7,
                      131800,
                      'DKSHKNS8JS76S39',
                      'VW',
                      'Fusca 78',
                      1978,
                      3,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      8,
                      151800,
                      'DKSHKNS8JS76S39',
                      'VW',
                      'Fusca 78',
                      1978,
                      3,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      9,
                      152800,
                      'DKSHKNS8JS76S39',
                      'VW',
                      'Fusca 78',
                      1978,
                      3,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      10,
                      211800,
                      'LKIUNS8JS76S39',
                      'Fiat',
                      'Fiat 147',
                      1996,
                      10,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      11,
                      212800,
                      'SSIUNS8JS76S39',
                      'Fiat',
                      'Fiat 147',
                      1996,
                      7,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      12,
                      21800,
                      'SKIUNS8JS76S39',
                      'Nissan',
                      'Versa',
                      2019,
                      6,
                      'Gasolina'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      13,
                      10000,
                      'AKIUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2019,
                      2,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      14,
                      20000,
                      'AKIUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2019,
                      2,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      15,
                      30000,
                      'AKIUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2019,
                      2,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      16,
                      40000,
                      'AKIUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2019,
                      2,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      17,
                      55000,
                      'LLLUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2020,
                      4,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      18,
                      56000,
                      'LLLUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2020,
                      4,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      19,
                      58000,
                      'LLLUNS1JS76S39',
                      'Nissan',
                      'Versa',
                      2020,
                      4,
                      'Etanol'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      20,
                      1800,
                      'AAAKNS8JS76S39',
                      'Toyota',
                      'Corolla XEI',
                      2023,
                      1,
                      'Flex'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      21,
                      8500,
                      'AAAKNS8JS76S39',
                      'Toyota',
                      'Corolla XEI',
                      2023,
                      1,
                      'Flex'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      22,
                      28000,
                      'MSLUNS1JS76S39',
                      'Nissan',
                      'Frontier',
                      2022,
                      5,
                      'Diesel'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      23,
                      38000,
                      'MSLUNS1JS76S39',
                      'Nissan',
                      'Frontier',
                      2022,
                      5,
                      'Diesel'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      24,
                      48000,
                      'MSLUNS1JS76S39',
                      'Nissan',
                      'Frontier',
                      2022,
                      5,
                      'Diesel'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      25,
                      68000,
                      'MSLUNS1JS76S39',
                      'Nissan',
                      'Frontier',
                      2022,
                      5,
                      'Diesel'
                  );

INSERT INTO Carro (
                      idCarro,
                      kmCarro,
                      classiCarro,
                      marcaCarro,
                      modeloCarro,
                      anoCarro,
                      idcombustivel,
                      tipoCombustivel
                  )
                  VALUES (
                      26,
                      78000,
                      'MSLUNS1JS76S39',
                      'Nissan',
                      'Frontier',
                      2022,
                      5,
                      'Diesel'
                  );


-- Table: Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    idCliente     INTEGER       NOT NULL
                                PRIMARY KEY,
    nomeCliente   VARCHAR (255) NOT NULL,
    cidadeCliente VARCHAR (255),
    estadoCliente VARCHAR (255),
    paisCliente   VARCHAR (255) 
);

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        1,
                        'Cliente dois',
                        'São Paulo',
                        'São Paulo',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        2,
                        'Cliente dois',
                        'São Paulo',
                        'São Paulo',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        3,
                        'Cliente tres',
                        'Rio de Janeiro',
                        'Rio de Janeiro',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        4,
                        'Cliente quatro',
                        'Rio de Janeiro',
                        'Rio de Janeiro',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        5,
                        'Cliente quatro',
                        'Rio de Janeiro',
                        'Rio de Janeiro',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        6,
                        'Cliente seis',
                        'Belo Horizonte',
                        'Minas Gerais',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        7,
                        'Cliente seis',
                        'Belo Horizonte',
                        'Minas Gerais',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        8,
                        'Cliente quatro',
                        'Rio de Janeiro',
                        'Rio de Janeiro',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        9,
                        'Cliente quatro',
                        'Rio de Janeiro',
                        'Rio de Janeiro',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        10,
                        'Cliente dez',
                        'Rio Branco',
                        'Acre',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        11,
                        'Cliente vinte',
                        'Macapá',
                        'Amapá',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        12,
                        'Cliente vinte',
                        'Macapá',
                        'Amapá',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        13,
                        'Cliente vinte e dois',
                        'Porto Alegre',
                        'Rio Grande do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        14,
                        'Cliente vinte e dois',
                        'Porto Alegre',
                        'Rio Grande do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        15,
                        'Cliente vinte e dois',
                        'Porto Alegre',
                        'Rio Grande do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        16,
                        'Cliente vinte e dois',
                        'Porto Alegre',
                        'Rio Grande do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        17,
                        'Cliente vinte e tres',
                        'Eusébio',
                        'Ceará',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        18,
                        'Cliente vinte e tres',
                        'Eusébio',
                        'Ceará',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        19,
                        'Cliente vinte e tres',
                        'Eusébio',
                        'Ceará',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        20,
                        'Cliente cinco',
                        'Manaus',
                        'Amazonas',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        21,
                        'Cliente cinco',
                        'Manaus',
                        'Amazonas',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        22,
                        'Cliente vinte e seis',
                        'Campo Grande',
                        'Mato Grosso do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        23,
                        'Cliente vinte e seis',
                        'Campo Grande',
                        'Mato Grosso do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        24,
                        'Cliente vinte e seis',
                        'Campo Grande',
                        'Mato Grosso do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        25,
                        'Cliente vinte e seis',
                        'Campo Grande',
                        'Mato Grosso do Sul',
                        'Brasil'
                    );

INSERT INTO Cliente (
                        idCliente,
                        nomeCliente,
                        cidadeCliente,
                        estadoCliente,
                        paisCliente
                    )
                    VALUES (
                        26,
                        'Cliente vinte e seis',
                        'Campo Grande',
                        'Mato Grosso do Sul',
                        'Brasil'
                    );


-- Table: Combustivel
CREATE TABLE IF NOT EXISTS Combustivel (
    idcombustivel   INTEGER       NOT NULL
                                  PRIMARY KEY,
    tipoCombustivel VARCHAR (255) 
);

INSERT INTO Combustivel (
                            idcombustivel,
                            tipoCombustivel
                        )
                        VALUES (
                            1,
                            'Gasolina'
                        );

INSERT INTO Combustivel (
                            idcombustivel,
                            tipoCombustivel
                        )
                        VALUES (
                            2,
                            'Etanol'
                        );

INSERT INTO Combustivel (
                            idcombustivel,
                            tipoCombustivel
                        )
                        VALUES (
                            3,
                            'Flex'
                        );

INSERT INTO Combustivel (
                            idcombustivel,
                            tipoCombustivel
                        )
                        VALUES (
                            4,
                            'Diesel'
                        );


-- Table: Locacao
CREATE TABLE IF NOT EXISTS Locacao (
    idLocacao   INTEGER NOT NULL
                        PRIMARY KEY,
    idCliente   INTEGER NOT NULL,
    idCarro     INTEGER NOT NULL,
    qtdDiaria   INTEGER,
    vlrDiaria   DECIMAL,
    dataLocacao DATE,
    horaLocacao TIME,
    idVendedor  INTEGER,
    FOREIGN KEY (
        idCliente
    )
    REFERENCES Cliente (idCliente),
    FOREIGN KEY (
        idCarro
    )
    REFERENCES Carro (idCarro),
    FOREIGN KEY (
        idVendedor
    )
    REFERENCES Vendedor (idVendedor) 
);

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        1,
                        2,
                        98,
                        2,
                        100,
                        20150110,
                        '10:00',
                        5
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        2,
                        2,
                        98,
                        2,
                        100,
                        20150210,
                        '12:00',
                        5
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        3,
                        3,
                        99,
                        2,
                        150,
                        20150213,
                        '12:00',
                        6
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        4,
                        4,
                        99,
                        5,
                        150,
                        20150215,
                        '13:00',
                        6
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        5,
                        4,
                        99,
                        5,
                        150,
                        20150302,
                        '14:00',
                        7
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        6,
                        6,
                        3,
                        10,
                        250,
                        20160302,
                        '14:00',
                        8
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        7,
                        6,
                        3,
                        10,
                        250,
                        20160802,
                        '14:00',
                        8
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        8,
                        4,
                        3,
                        10,
                        250,
                        20170102,
                        '18:00',
                        6
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        9,
                        4,
                        3,
                        10,
                        280,
                        20180102,
                        '18:00',
                        6
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        10,
                        10,
                        10,
                        10,
                        50,
                        20180302,
                        '18:00',
                        16
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        11,
                        20,
                        7,
                        10,
                        50,
                        20180401,
                        '11:00',
                        16
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        12,
                        20,
                        6,
                        10,
                        150,
                        20200401,
                        '11:00',
                        16
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        13,
                        22,
                        2,
                        20,
                        150,
                        20220501,
                        '8:00',
                        30
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        14,
                        22,
                        2,
                        20,
                        150,
                        20220601,
                        '8:00',
                        30
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        15,
                        22,
                        2,
                        20,
                        150,
                        20220701,
                        '8:00',
                        30
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        16,
                        22,
                        2,
                        20,
                        150,
                        20220801,
                        '8:00',
                        30
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        17,
                        23,
                        4,
                        20,
                        150,
                        20220901,
                        '8:00',
                        31
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        18,
                        23,
                        4,
                        20,
                        150,
                        20221001,
                        '8:00',
                        31
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        19,
                        23,
                        4,
                        20,
                        150,
                        20221101,
                        '8:00',
                        31
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        20,
                        5,
                        1,
                        10,
                        880,
                        20230102,
                        '18:00',
                        16
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        21,
                        5,
                        1,
                        10,
                        880,
                        20230115,
                        '18:00',
                        16
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        22,
                        26,
                        5,
                        5,
                        600,
                        20230125,
                        '8:00',
                        32
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        23,
                        26,
                        5,
                        5,
                        600,
                        20230131,
                        '8:00',
                        32
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        24,
                        26,
                        5,
                        5,
                        600,
                        20230206,
                        '8:00',
                        32
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        25,
                        26,
                        5,
                        5,
                        600,
                        20230212,
                        '8:00',
                        32
                    );

INSERT INTO Locacao (
                        idLocacao,
                        idCliente,
                        idCarro,
                        qtdDiaria,
                        vlrDiaria,
                        dataLocacao,
                        horaLocacao,
                        idVendedor
                    )
                    VALUES (
                        26,
                        26,
                        5,
                        1,
                        600,
                        20230218,
                        '8:00',
                        32
                    );


-- Table: Vendedor
CREATE TABLE IF NOT EXISTS Vendedor (
    idVendedor     INTEGER       NOT NULL
                                 PRIMARY KEY,
    nomeVendedor   VARCHAR (255),
    sexoVendedor   SMALLINT (1),
    estadoVendedor VARCHAR (255) 
);

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         5,
                         'Vendedor cinco',
                         0,
                         'São Paulo'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         6,
                         'Vendedora seis',
                         1,
                         'São Paulo'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         7,
                         'Vendedora sete',
                         1,
                         'Rio de Janeiro'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         8,
                         'Vendedora oito',
                         1,
                         'Minas Gerais'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         16,
                         'Vendedor dezesseis',
                         0,
                         'Amazonas'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         30,
                         'Vendedor trinta',
                         0,
                         'Rio Grande do Sul'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         31,
                         'Vendedor trinta e um',
                         0,
                         'Ceará'
                     );

INSERT INTO Vendedor (
                         idVendedor,
                         nomeVendedor,
                         sexoVendedor,
                         estadoVendedor
                     )
                     VALUES (
                         32,
                         'Vendedora trinta e dois',
                         1,
                         'Mato Grosso do Sul'
                     );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
