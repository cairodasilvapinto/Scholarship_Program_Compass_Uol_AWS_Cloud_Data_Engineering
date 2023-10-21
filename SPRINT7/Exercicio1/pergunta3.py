import pandas as pd
import numpy as np

# Carregar os dados
data = pd.read_csv("actors.csv")

# Calculando a média por filme para cada ator/atriz
data["media_por_filme"] = data["Total Gross"] / data["Number of Movies"]

# Encontrando o ator/atriz com a maior média por filme
ator_maior_media = data.loc[data["media_por_filme"].idxmax(), "Actor"]

# Salvar resultado em arquivo .txt
with open("pergunta3.txt", "w", encoding="utf-8") as file:
    file.write(f"Ator/atriz com maior média de filme é {ator_maior_media}")
