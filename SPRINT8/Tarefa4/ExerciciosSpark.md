# Versões posteriores a ultima etapa do exercicio 4
```python
#codigo python de Tarefa 4: Exercícios - Apache Spark - até parte 6
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, floor, col

# Definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv
df_nomes = spark.read.csv("nomes_aleatorios.txt")

# Renomear a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprimir o esquema do DataFrame
df_nomes.printSchema()

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

# Selecionar as pessoas que nasceram neste século
df_select = df_nomes.select("*").where(col("AnoNascimento") >= 2000)

# Mostrar as primeiras 10 linhas do DataFrame
df_select.show(10)
```

```python
# parte 7
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand, floor, col

# Definir a Spark Session
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

# Execute a consulta SQL para selecionar as pessoas que nasceram neste século
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Mostrar as primeiras 10 linhas do resultado
df_select_sql.show(10)
```

```python
# parte 8
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, floor, col

# Definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv
df_nomes = spark.read.csv("nomes_aleatorios.txt")

# Renomear a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

# Adicionar nova coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn('Escolaridade', 
                               when(rand() < 0.33, 'Fundamental').otherwise(
                               when(rand() < 0.5, 'Medio').otherwise('Superior')))

# Lista de países da América do Sul
paises = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 
          'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 
          'Guiana Francesa']

# Adicionar nova coluna 'Pais' com valores aleatórios
df_nomes = df_nomes.withColumn('Pais',
                               when(rand() < 1/13, paises[0]).otherwise(
                               when(rand() < 2/13, paises[1]).otherwise(
                               when(rand() < 3/13, paises[2]).otherwise(
                               when(rand() < 4/13, paises[3]).otherwise(
                               when(rand() < 5/13, paises[4]).otherwise(
                               when(rand() < 6/13, paises[5]).otherwise(
                               when(rand() < 7/13, paises[6]).otherwise(
                               when(rand() < 8/13, paises[7]).otherwise(
                               when(rand() < 9/13, paises[8]).otherwise(
                               when(rand() < 10/13, paises[9]).otherwise(
                               when(rand() < 11/13, paises[10]).otherwise(
                               when(rand() < 12/13, paises[11]).otherwise(paises[12])))))))))))))

# Adicionar nova coluna 'AnoNascimento' com valores aleatórios
df_nomes = df_nomes.withColumn('AnoNascimento', floor(rand() * (2010 - 1945 + 1) + 1945))

# Registre o DataFrame como uma tabela temporária chamada "pessoas"
df_nomes.createOrReplaceTempView("pessoas")

# Execute a consulta SQL para selecionar as pessoas que nasceram neste século
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Use o método select para selecionar as pessoas que são da geração Millennials
df_millennials = df_nomes.select('*').where((col('AnoNascimento') >= 1980) & (col('AnoNascimento') <= 1994))

# Conte o número de pessoas que são da geração Millennials
num_millennials = df_millennials.count()

print("Número de pessoas que são da geração Millennials: ", num_millennials)
```

```python
# parte 9
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, floor, col

# Definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv
df_nomes = spark.read.csv("nomes_aleatorios.txt")

# Renomear a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

# Adicionar nova coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn('Escolaridade', 
                               when(rand() < 0.33, 'Fundamental').otherwise(
                               when(rand() < 0.5, 'Medio').otherwise('Superior')))

# Lista de países da América do Sul
paises = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 
          'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 
          'Guiana Francesa']

# Adicionar nova coluna 'Pais' com valores aleatórios
df_nomes = df_nomes.withColumn('Pais',
                               when(rand() < 1/13, paises[0]).otherwise(
                               when(rand() < 2/13, paises[1]).otherwise(
                               when(rand() < 3/13, paises[2]).otherwise(
                               when(rand() < 4/13, paises[3]).otherwise(
                               when(rand() < 5/13, paises[4]).otherwise(
                               when(rand() < 6/13, paises[5]).otherwise(
                               when(rand() < 7/13, paises[6]).otherwise(
                               when(rand() < 8/13, paises[7]).otherwise(
                               when(rand() < 9/13, paises[8]).otherwise(
                               when(rand() < 10/13, paises[9]).otherwise(
                               when(rand() < 11/13, paises[10]).otherwise(
                               when(rand() < 12/13, paises[11]).otherwise(paises[12])))))))))))))

# Adicionar nova coluna 'AnoNascimento' com valores aleatórios
df_nomes = df_nomes.withColumn('AnoNascimento', floor(rand() * (2010 - 1945 + 1) + 1945))

# Registre o DataFrame como uma tabela temporária chamada "pessoas"
df_nomes.createOrReplaceTempView("pessoas")

# Execute a consulta SQL para selecionar as pessoas que nasceram neste século
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Execute a consulta SQL para selecionar as pessoas que são da geração Millennials
df_millennials_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")

# Conte o número de pessoas que são da geração Millennials
num_millennials_sql = df_millennials_sql.count()

print("Número de pessoas que são da geração Millennials: ", num_millennials_sql)
```