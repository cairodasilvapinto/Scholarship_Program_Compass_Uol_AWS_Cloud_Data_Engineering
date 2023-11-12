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

# Lendo os dados CSV da Raw Zone
movies_csv_df = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", "|")
    .load("s3://desafioetl1/desafioetl1/Raw/Local/CSV/Movies/2023/10/21/movies.csv")
)

# Escrevendo os dados CSV transformados na Trusted Zone no formato PARQUET
movies_csv_df.write.parquet("s3://desafioetl1/desafioetl1/trusted/movies.parquet")
