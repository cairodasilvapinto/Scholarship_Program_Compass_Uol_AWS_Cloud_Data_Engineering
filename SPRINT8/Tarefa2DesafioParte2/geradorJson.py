import json
import requests
import boto3
from datetime import date


def lambda_handler(event, context):
    # Crie o cliente S3 especificando a região
    s3 = boto3.client("s3", region_name="us-east-1")

    # Fazendo uma chamada API ao TMDB
    url_discover = "https://api.themoviedb.org/3/discover/movie"
    url_movie = "https://api.themoviedb.org/3/movie/"
    querystring = {
        "api_key": "a4b19d34fb649042fb1473575842df56",
        "language": "pt-BR",
        "sort_by": "vote_average.desc",
        "include_adult": "false",
        "include_video": "false",
        "primary_release_date.gte": "2020-01-01",
        "primary_release_date.lte": str(date.today()),
        "vote_count.gte": "500",
        "with_genres": "16,35",  # 16 para Animação e 35 para Comédia
    }

    all_movies = []
    for page in range(1, 11):
        querystring["page"] = str(page)
        response_discover = requests.request("GET", url_discover, params=querystring)
        data_discover = response_discover.json()

        # Para cada filme, obtenha os detalhes do filme
        for result in data_discover["results"]:
            querystring["append_to_response"] = "credits"
            response_movie = requests.request(
                "GET", url_movie + str(result["id"]), params=querystring
            )
            data_movie = response_movie.json()
            movie_details = {
                "id": data_movie["id"],
                "title": data_movie["title"],
                "revenue": data_movie["revenue"],
                "budget": data_movie["budget"],
                "vote_average": data_movie["vote_average"],
                "vote_count": data_movie["vote_count"],
                "genres": data_movie["genres"],
                "release_date": data_movie["release_date"],
                "main_actor": next(
                    (
                        cast["name"]
                        for cast in data_movie["credits"]["cast"]
                        if cast["order"] == 0
                    ),
                    None,
                ),
                "director": next(
                    (
                        crew["name"]
                        for crew in data_movie["credits"]["crew"]
                        if crew["job"] == "Director"
                    ),
                    None,
                ),
            }
            all_movies.append(movie_details)

        # Dividindo os dados em grupos de 100 registros
        chunks = [all_movies[i : i + 100] for i in range(0, len(all_movies), 100)]

        for i, chunk in enumerate(chunks):
            # Gravando os dados no S3
            s3.put_object(
                Body=json.dumps(chunk),
                Bucket="desafioetl1",
                Key=f"desafioetl1/Raw/tmdb/json/2023/11/12{page}_{i}.json",
            )

    return {"statusCode": 200, "body": json.dumps("Dados gravados com sucesso no S3!")}
