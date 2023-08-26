# Ler o conteúdo do arquivo actors.csv
with open("actors.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0]
data = lines[1:]


# Etapa 3: Encontrar o ator/atriz com a maior média de receita bruta por filme
def get_actor_and_average_gross(line):
    data = line.split(",")
    actor = data[0].strip(' "')
    average_gross = float(data[-3].strip())
    return actor, average_gross


actor_with_highest_average = max(
    data, key=lambda line: get_actor_and_average_gross(line)[1]
)
actor_name_highest_average, highest_average_gross = get_actor_and_average_gross(
    actor_with_highest_average
)

# Salvar resultado da etapa 3 em arquivo .txt
with open("etapa-3.txt", "w", encoding="utf-8") as file:
    file.write(
        f"O ator/atriz com a maior média de receita bruta por filme é {actor_name_highest_average} com média de {highest_average_gross:.2f} milhões."
    )
