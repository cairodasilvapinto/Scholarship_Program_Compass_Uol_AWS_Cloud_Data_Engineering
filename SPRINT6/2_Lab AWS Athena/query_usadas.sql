-- Query para criar o banco de dados
CREATE DATABASE meubanco

-- Query para criar as tabelas
CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes ( 
    `nome` STRING,
    `sexo` STRING,
    `total` INT,
    `ano` INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ( 
    'serialization.format' = ',',
    'field.delim' = ','
)
LOCATION 's3://labawss3.com/dados'

-- Query test
select nome from meubanco.nomes where ano = 1999 order by total limit 15

-- Query do exercicio
WITH
  nomes_por_decada AS (
    SELECT
      ano,
      nome,
      total,
      ROW_NUMBER() OVER (PARTITION BY ano ORDER BY total DESC) AS toptres
    FROM
      meubanco.nomes
    WHERE
      ano >= 1950
  ),
  nomes_mais_usados AS (
    SELECT
      ano,
      nome
    FROM
      nomes_por_decada
    WHERE
      toptres <= 3
  )
SELECT
  ano,
  nome
FROM
  nomes_mais_usados
ORDER BY
  ano