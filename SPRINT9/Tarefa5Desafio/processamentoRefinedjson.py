# Antes de executar este script, certifique-se de que o crawler já foi executado
# e que a tabela está disponível no catálogo do Glue.
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Inicializando o GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# Lendo os dados da tabela criada pelo crawler
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="teste", table_name="dt_2023_11_12"
)

# Convertendo o DynamicFrame apara um DataFrame
dataframe = dynamic_frame.toDF()

# Filtrando as linhas onde 'budget' e 'revenue' são diferentes de zero
# As linhas com 0 não seram consideradas na tabela de fatos
# Somente as linhas onde ambos budget e revenue são diferentes de zero serão mantidas

dataframe = dataframe.filter((dataframe.budget != 0) & (dataframe.revenue != 0))

# Criando as tabelas de dimensões e a tabela de fatos
dim_artista = dataframe.select("id", "main_actor", "director").dropDuplicates()
dim_filme = dataframe.select("id", "title", "release_date").dropDuplicates()
fato_filmes = dataframe.select("id", "budget", "revenue", "vote_average", "vote_count").dropDuplicates()

# Escrevendo os dados nas tabelas correspondentes na camada Refined
dim_artista.write.parquet("s3://desafioetl1/desafioetl1/refined/dim_artista")
dim_filme.write.parquet("s3://desafioetl1/desafioetl1/refined/dim_filme")
fato_filmes.write.parquet("s3://desafioetl1/desafioetl1/refined/fato_filmes")
