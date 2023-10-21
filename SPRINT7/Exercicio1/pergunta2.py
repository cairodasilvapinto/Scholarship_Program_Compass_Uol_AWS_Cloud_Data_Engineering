import pandas as pd
import numpy as np

# Carregar os dados
data = pd.read_csv("actors.csv")

# Tratar o erro no registro do ator "Robert Downey Jr."
data.loc[data["Actor"] == '"Robert Downey, Jr."', "Number of Movies"] = 53

# Calcular a média do número de filmes
average_movies = np.mean(data["Number of Movies"])

# Salvar resultado em arquivo .txt
with open("pergunta2.txt", "w", encoding="utf-8") as file:
    file.write(f"A média do número de filmes é {average_movies:.2f}")
