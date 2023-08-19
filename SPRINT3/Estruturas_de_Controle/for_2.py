palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end=",")
print("Fim")

aprovados = ["Ana", "Carlos", "Pedro", "Julia"]
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f"{posicao + 1})", nome)

dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
for dia in dias_semana:
    print(f"O dia da semana é {dia}")

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
