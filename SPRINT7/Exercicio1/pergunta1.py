import pandas as pd
import numpy as np

# Carregar os dados
data = pd.read_csv("actors.csv")

# Tratar o erro no registro do ator "Robert Downey Jr."
data.loc[data["Actor"] == "Robert Downey Jr.", "Number of Movies"] = 1

# Encontrar o ator com o maior número de filmes
max_movies_actor = data.loc[data["Number of Movies"].idxmax()]

# Salvar resultado em arquivo .txt
with open("pergunta1.txt", "w", encoding="utf-8") as file:
    file.write(
        f"O ator {max_movies_actor['Actor']} tem {max_movies_actor['Number of Movies']} filmes."
    )
