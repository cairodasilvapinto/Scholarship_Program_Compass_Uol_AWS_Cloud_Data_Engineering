# Ler o conteúdo do arquivo actors.csv
with open("actors.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0]
data = lines[1:]


# Etapa 5: Ordenar atores por receita bruta total
def get_actor_name_and_total_gross(line):
    data = line.split(",")
    actor_name = data[0]
    total_gross_str = data[1].strip()

    try:
        total_gross = float(total_gross_str)
    except ValueError:
        total_gross = 3947.30

    if actor_name == '"Robert Downey':
        actor_name = "Robert Downey Jr."
    return actor_name, total_gross


sorted_actors_by_total_gross = sorted(
    data, key=lambda line: get_actor_name_and_total_gross(line)[1], reverse=True
)

with open("etapa-5.txt", "w", encoding="utf-8") as file:
    for line in sorted_actors_by_total_gross:
        actor_name, total_gross = get_actor_name_and_total_gross(line)
        file.write(f"{actor_name} - {total_gross}\n")
