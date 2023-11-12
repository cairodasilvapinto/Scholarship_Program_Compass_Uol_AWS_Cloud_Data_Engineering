import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import lit

# Inicializando o GlueContext e a sessão Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Lendo todos os arquivos .json da Raw Zone
for i in range(1, 11):  # Loop de 1 a 10
    file_path = f"desafioetl1/desafioetl1/Raw/tmdb/json/2023/11/12/{i}_0.json"
    movies_json_df = spark.read.json(f"s3://{file_path}")

    # Extraindo a data completa do caminho do arquivo
    date = "-".join(file_path.split("/")[4:8])

    # Adicionando a coluna 'dt' ao DataFrame
    movies_json_df = movies_json_df.withColumn("dt", lit(date))

    # Escrevendo os dados JSON transformados na Trusted Zone no formato PARQUET
    movies_json_df.write.partitionBy("dt").parquet(
        f"s3://desafioetl1/desafioetl1/trusted/{date}/movies_json_{i}.parquet"
    )
