import boto3
import os
from datetime import datetime

s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIAR5MNFZDVTITMPU64",
    aws_secret_access_key="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",
)

bucket_name = "desafioetl1"
raw_zone = "Raw"
local_data = "Local"
data_format = "CSV"
data_specification = "Series"
data_processing_date = datetime.now().strftime("%Y/%m/%d")

source_file_name = "series.csv"

s3_destination_path = f"desafioetl1/Raw/Local/CSV/Series/2023/10/02/series.csv"
local_file_path = (
    "C:/Users/cairo/bolsaCOMPASS/SPRINT7/Desafio Parte 1/Filmes+e+Series/series.csv"
)

s3.upload_file(local_file_path, bucket_name, s3_destination_path)
