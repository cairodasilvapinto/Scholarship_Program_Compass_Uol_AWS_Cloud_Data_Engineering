# ultima parte do exercicio 4(parte 10)
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, floor, col

# Definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv
df_nomes = spark.read.csv("nomes_aleatorios.txt")

# Renomear a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adicionar nova coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").otherwise(
        when(rand() < 0.5, "Medio").otherwise("Superior")
    ),
)

# Lista de países da América do Sul
paises = [
    "Argentina",
    "Bolívia",
    "Brasil",
    "Chile",
    "Colômbia",
    "Equador",
    "Guiana",
    "Paraguai",
    "Peru",
    "Suriname",
    "Uruguai",
    "Venezuela",
    "Guiana Francesa",
]

# Adicionar nova coluna 'Pais' com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 1 / 13, paises[0]).otherwise(
        when(rand() < 2 / 13, paises[1]).otherwise(
            when(rand() < 3 / 13, paises[2]).otherwise(
                when(rand() < 4 / 13, paises[3]).otherwise(
                    when(rand() < 5 / 13, paises[4]).otherwise(
                        when(rand() < 6 / 13, paises[5]).otherwise(
                            when(rand() < 7 / 13, paises[6]).otherwise(
                                when(rand() < 8 / 13, paises[7]).otherwise(
                                    when(rand() < 9 / 13, paises[8]).otherwise(
                                        when(rand() < 10 / 13, paises[9]).otherwise(
                                            when(
                                                rand() < 11 / 13, paises[10]
                                            ).otherwise(
                                                when(
                                                    rand() < 12 / 13, paises[11]
                                                ).otherwise(paises[12])
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    ),
)

# Adicionar nova coluna 'AnoNascimento' com valores aleatórios
df_nomes = df_nomes.withColumn(
    "AnoNascimento", floor(rand() * (2010 - 1945 + 1) + 1945)
)

# Registre o DataFrame como uma tabela temporária chamada "pessoas"
df_nomes.createOrReplaceTempView("pessoas")

# Execute a consulta SQL para obter a quantidade de pessoas de cada país para cada geração
df_geracoes = spark.sql(
    """
    SELECT Pais,
           CASE
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
           END AS Geracao,
           COUNT(*) as Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
"""
)

# Mostrar todas as linhas do DataFrame
df_geracoes.show()
