import sys
from awsglue.transforms import *
from pyspark.sql.functions import upper, desc, max
from pyspark.sql import functions as F
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_INPUT_PATH", "S3_TARGET_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = args["S3_INPUT_PATH"]
target_path = args["S3_TARGET_PATH"]

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator": ","},
)

# Aqui está sendo criado um dataframe Spark a partir de um dataframe dinâmico glue
spark_df = df.toDF()

# Imprimir o schema do dataframe
spark_df.printSchema()

# Alterar a caixa dos valores da coluna 'nome' para maiúsculo
spark_df = spark_df.withColumn("nome", upper(F.col("nome")))

# Imprimir a contagem de linhas presentes no dataframe
print("Número de linhas no dataframe: ", spark_df.count())

# Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
spark_df.groupBy("ano", "sexo").count().show()

# Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.
spark_df = spark_df.orderBy(desc("ano"))

# Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
feminino_max = (
    spark_df.filter(spark_df.sexo == "F")
    .groupBy("nome", "ano")
    .count()
    .orderBy(desc("count"))
    .first()
)
print(
    f"O nome feminino com mais registros foi {feminino_max['nome']} e ocorreu no ano {feminino_max['ano']}"
)

# Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
masculino_max = (
    spark_df.filter(spark_df.sexo == "M")
    .groupBy("nome", "ano")
    .count()
    .orderBy(desc("count"))
    .first()
)
print(
    f"O nome masculino com mais registros foi {masculino_max['nome']} e ocorreu no ano {masculino_max['ano']}"
)

# Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe.
total_registros_por_ano = spark_df.groupBy("ano").count().orderBy("ano").limit(10)
total_registros_por_ano.show()

# Converter o DataFrame do Spark de volta para um DynamicFrame antes de escrever para o S3
saida = DynamicFrame.fromDF(spark_df, glueContext, "saida")

glueContext.write_dynamic_frame.from_options(
    frame=saida,
    connection_type="s3",
    connection_options={"path": target_path, "partitionKeys": ["sexo", "ano"]},
    format="json",
)
