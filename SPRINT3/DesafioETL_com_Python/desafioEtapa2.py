# Ler o conteúdo do arquivo actors.csv
with open("actors.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0]
data = lines[1:]


# Etapa 2: Calcular a média de receita bruta dos principais filmes
def get_gross(line):
    data = line.split(",")
    gross_value = float(data[-1].strip())
    return gross_value


gross_values = [get_gross(line) for line in data]
average_gross = sum(gross_values) / len(gross_values)

# Salvar resultado da etapa 2 em arquivo .txt
with open("etapa-2.txt", "w", encoding="utf-8") as file:
    file.write(
        f"A média de receita bruta dos principais filmes é {average_gross:.2f} milhões."
    )
