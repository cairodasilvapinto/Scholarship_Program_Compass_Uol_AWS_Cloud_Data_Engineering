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
WITH nomes_por_decada AS (
  SELECT
    nome,
    ano - (ano % 10) AS decada,
    SUM(total) AS total_por_decada
  FROM
    meubanco.nomes
  WHERE
    ano >= 1950
  GROUP BY
    nome, ano - (ano % 10)
),
ranked_nomes_por_decada AS (
  SELECT
    decada,
    nome,
    total_por_decada,
    ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total_por_decada DESC) AS rank
  FROM
    nomes_por_decada
)
SELECT
  CASE
    WHEN (decada % 10 = 0) THEN CAST(decada AS VARCHAR)
    ELSE CAST(decada AS VARCHAR) || 's'
  END AS decada,
  nome,
  total_por_decada
FROM
  ranked_nomes_por_decada
WHERE
  rank <= 3
ORDER BY
  decada, rank;
