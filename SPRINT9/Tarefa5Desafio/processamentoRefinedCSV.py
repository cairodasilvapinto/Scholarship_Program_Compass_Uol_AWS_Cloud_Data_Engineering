# passando para refined apenas os dados vindos do CSV que são do genero do genero Comedy e Animation
# apenas as linhas que não apresentão valores nulos \N
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col
from pyspark.sql.functions import array_contains, split

# Inicializando o GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# Lendo os dados da tabela criada pelo crawler
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="teste", table_name="movies_parquet"
)

# Convertendo o DynamicFrame para um DataFrame
dataframe = dynamic_frame.toDF()

# Dividindo a coluna de gênero em uma lista
dataframe = dataframe.withColumn("genero", split(col("genero"), ","))

# Filtrando os filmes de gênero Comedy e Animation
dataframe = dataframe.filter(
    array_contains(col("genero"), "Comedy") | array_contains(col("genero"), "Animation")
)

# Removendo as linhas com valores nulos
dataframe = dataframe.filter(col("generoArtista") != "\\N")
dataframe = dataframe.filter(col("personagem") != "\\N")
dataframe = dataframe.filter(col("nomeArtista") != "\\N")
dataframe = dataframe.filter(col("anoNascimento") != "\\N")
dataframe = dataframe.filter(col("anoFalecimento") != "\\N")
dataframe = dataframe.filter(col("profissao") != "\\N")
dataframe = dataframe.filter(col("titulosMaisConhecidos") != "\\N")

# Criando as tabelas de dimensões e a tabela de fatos
dim_artista = dataframe.select(
    "id", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao"
)
dim_filme = dataframe.select(
    "id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero"
)
fato_filmes = dataframe.select("id", "notaMedia", "numeroVotos")

# Escrevendo os dados nas tabelas correspondentes na camada Refined
dim_artista.write.parquet("s3://desafioetl1/desafioetl1/refined/CSVdim_artista")
dim_filme.write.parquet("s3://desafioetl1/desafioetl1/refined/CSVdim_filme")
fato_filmes.write.parquet("s3://desafioetl1/desafioetl1/refined/CSVfato_filmes")
