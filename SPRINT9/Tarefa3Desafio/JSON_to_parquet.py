from pyspark import SparkContext, SparkConf
from awsglue.context import GlueContext
from pyspark import SparkContext, SparkConf
from awsglue.context import GlueContext
from pyspark.sql import DataFrame
from pyspark.sql.functions import lit

# Inicializando o GlueContext e a sessão Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Lendo o primeiro arquivo .json da Raw Zone para obter o esquema
file_path = "desafioetl1/desafioetl1/Raw/tmdb/json/2023/11/12/50_0.json"
first_df = spark.read.json(f"s3://{file_path}")

# DataFrame vazio para armazenar todos os dados
all_data_df = spark.createDataFrame([], first_df.schema)

# Lendo todos os arquivos .json da Raw Zone
for i in range(0, 2):  # Loop de 1 a 10
    file_path = f"desafioetl1/desafioetl1/Raw/tmdb/json/2023/11/12/50_{i}.json"
    movies_json_df = spark.read.json(f"s3://{file_path}")

    # Extraindo a data completa do caminho do arquivo
    date = "-".join(file_path.split("/")[5:8])

    # Adicionando a coluna 'dt' ao DataFrame
    movies_json_df = movies_json_df.withColumn("dt", lit(date))

    # Adicionando os dados ao DataFrame geral
    all_data_df = all_data_df.unionByName(movies_json_df, allowMissingColumns=True)

# Escrevendo os dados JSON transformados na Trusted Zone no formato PARQUET
all_data_df.write.partitionBy("dt").parquet(
    f"s3://desafioetl1/desafioetl1/trusted/movies_json.parquet"
)
