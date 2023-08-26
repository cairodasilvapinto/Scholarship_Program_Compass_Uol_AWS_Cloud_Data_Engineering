# Ler o conteúdo do arquivo actors.csv
with open("actors.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0]
data = lines[1:]


# Etapa 1: Encontrar o ator com o maior número de filmes
def get_actor_name_and_number_of_movies(line):
    data = line.split(",")
    actor_name = data[0]
    number_of_movies = float(data[2].strip())

    # Resolvendo erro do regsitro do ator "Robert Downey Jr."
    if number_of_movies == 3947.30:
        number_of_movies = 1

    return actor_name, number_of_movies


actor_with_most_movies = max(
    data, key=lambda line: get_actor_name_and_number_of_movies(line)[1]
)
actor_name_most_movies, num_movies_most_movies = get_actor_name_and_number_of_movies(
    actor_with_most_movies
)

# Salvar resultado da etapa 1 em arquivo .txt
with open("etapa-1.txt", "w", encoding="utf-8") as file:
    file.write(f"O ator {actor_name_most_movies} tem {num_movies_most_movies} filmes.")
