import numpy as np
import pandas as pd

# Carregar os dados
df = pd.read_csv("actors.csv")

# pega a frequencia de cada filme
movie_counts = df["#1 Movie"].value_counts()

# Seleciona os filmes com frequência maior que 1
frequent_movies = movie_counts[movie_counts > 1]

# Salvar resultado em arquivo .txt
with open("pergunta4.txt", "w") as file:
    file.write("Filmes com mais de 1 frequencia e suas frequencias:\n")
    for movie, count in frequent_movies.items():
        file.write(f"{movie}: {count}\n")
