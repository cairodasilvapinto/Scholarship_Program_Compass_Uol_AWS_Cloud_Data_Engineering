# Ler o conteúdo do arquivo actors.csv
with open("actors.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0]
data = lines[1:]

# Etapa 4: Contagem de aparições dos filmes de maior bilheteria
top_movies = [line.split(",")[-2].strip(' "') for line in data]
movies_count = {}
for movie in top_movies:
    if movie in movies_count:
        movies_count[movie] += 1
    else:
        movies_count[movie] = 1
sorted_movies_counts = sorted(
    movies_count.items(), key=lambda item: (item[1], item[0]), reverse=True
)

with open("etapa-4.txt", "w", encoding="utf-8") as file:
    for index, (movie, count) in enumerate(sorted_movies_counts, start=1):
        file.write(f"{index} - O filme {movie} aparece {count} vez(es) no dataset.\n")
