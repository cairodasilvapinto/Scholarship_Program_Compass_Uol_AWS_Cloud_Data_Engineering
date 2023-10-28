# Passo 1: Instalar a biblioteca names

# Passo 2: Importar as bibliotecas necessárias
import random
import time
import os
import names

# Passo 3: Definir os parâmetros para a geração do dataset
random.seed(40)  # Define a semente de aleatoriedade
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar os nomes aleatórios
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Passo 5: Gerar um arquivo de texto contendo todos os nomes
with open("nomes_aleatorios.txt", "w") as f:
    for nome in dados:
        f.write("%s\n" % nome)
