import boto3
import os
from datetime import datetime


def upload_file_to_s3(
    aws_access_key_id,
    aws_secret_access_key,
    bucket_name,
    raw_zone,
    local_data,
    data_format,
    data_specification,
    source_file_name,
    local_file_path,
):
    # Configura o cliente boto3
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    # Obtém a data de processamento
    data_processing_date = datetime.now().strftime("%Y/%m/%d")

    # Define o caminho de destino no S3
    s3_destination_path = f"{bucket_name}/{raw_zone}/{local_data}/{data_format}/{data_specification}/{data_processing_date}/{source_file_name}"

    # Faz o upload do arquivo para o S3
    s3.upload_file(local_file_path, bucket_name, s3_destination_path)


if __name__ == "__main__":
    # Configurações para o arquivo 'series.csv'
    upload_file_to_s3(
        aws_access_key_id="AKIAR5MNFZDVTITMPU64",
        aws_secret_access_key="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",
        bucket_name="desafioetl1",
        raw_zone="Raw",
        local_data="Local",
        data_format="CSV",
        data_specification="Series",
        source_file_name="series.csv",
        local_file_path="Filmes+e+Series/series.csv",
    )

    # Configurações para o arquivo 'movies.csv'
    upload_file_to_s3(
        aws_access_key_id="AKIAR5MNFZDVTITMPU64",
        aws_secret_access_key="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",
        bucket_name="desafioetl1",
        raw_zone="Raw",
        local_data="Local",
        data_format="CSV",
        data_specification="Movies",
        source_file_name="movies.csv",
        local_file_path="Filmes+e+Series/movies.csv",
    )

    print("Os arquivos foram carregados para o S3 com sucesso.")
