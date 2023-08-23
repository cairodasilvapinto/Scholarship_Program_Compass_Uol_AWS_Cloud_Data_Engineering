# E6

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list(set(a) & set(b)))

# E7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([n for n in a if n % 2 != 0])

# E8

palavras = ["maça", "arara", "audio", "radio", "radar", "moto"]
for palavra in palavras:
    if palavra == palavra[::-1]:  # palavra ao contrario
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")

# E9

# Você deve Utilizar a função enumerate().
primeirosNomes = ["Joao", "Douglas", "Lucas", "José"]
sobreNomes = ["Soares", "Souza", "Silveira", "Pedreira"]
idades = [19, 28, 25, 31]
for i, (primeirosNomes, sobreNomes, idades) in enumerate(
    zip(primeirosNomes, sobreNomes, idades)
):
    print(f"{i} - {primeirosNomes} {sobreNomes} está com {idades} anos")

# E10


def remove_duplidados_de_listas(lista):
    return list(set(lista))


lista = ["abc", "abc", "abc", "123", "abc", "123", "123"]
lista = remove_duplidados_de_listas(lista)
print(lista)

# E11

nome_arquivo = "arquivo_texto.txt"

try:
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo, end="")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

# E12

import json

arquivo_person = "person.json"

try:
    with open(arquivo_person, "r") as arquivo:
        conteudo = json.load(arquivo)  # Faz o parsing do JSON
        print(conteudo)  # Imprime o conteúdo completo do JSON

except FileNotFoundError:
    print(f"Arquivo {arquivo_person} não encontrado.")

# E13


def my_map(lista, funcao):
    return [funcao(elemento) for elemento in lista]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = my_map(lista, lambda x: x**2)
print(lista)

# E14
# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
# Teste sua função com os seguintes parâmetros:
# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
# A saída deve receber um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprimir o valor de cada parâmetro recebido

# *args e **kwargs são parâmetros especiais que podem ser passados para uma função.
# o *args é utilizado para passar um número variável de argumentos posicionais.
# enquanto o **kwargs é utilizado para passar um número variável de argumentos nomeados.


def funcao(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(value)


funcao(1, 3, 4, "hello", parametro_nomeado="alguma coisa", x=20)

# E15


class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


lampada = Lampada(False)
lampada.liga()
print(f"A lâmpada está ligada? {lampada.esta_ligada()}")
lampada.desliga()
print(f"A lâmpada ainda está ligada? {lampada.esta_ligada()}")

# E16


def soma_numeros_string(string_numeros):
    numeros = string_numeros.split(",")
    numeros = [int(num) for num in numeros]
    soma = sum(numeros)
    return soma


string_numeros = "1,3,4,6,10,76"

# Calcula a soma dos números na string
soma = soma_numeros_string(string_numeros)

print(soma)

# E17

"""
# maneira correta também, mas não passa no exercicio
def divide_lista_em_partes_iguais(lista):
    tamanho_parte = len(lista) // 3  # Calcula o tamanho de cada parte
    partes = [lista[i:i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]
    return partes

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes_divididas = divide_lista_em_partes_iguais(lista)

for parte in partes_divididas:
    print(parte, end=" ")
"""


def divide_lista_em_partes_iguais(lista):
    tamanho_parte = len(lista) // 3  # Calcula o tamanho de cada parte
    partes = [lista[i : i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]
    return partes


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes_divididas = divide_lista_em_partes_iguais(lista)

# Imprime do jeito que o exercicio pede
for i, parte in enumerate(partes_divididas):
    if i == len(partes_divididas) - 1:
        print(parte, end="\n")  # Adiciona \n no final da última parte
    else:
        print(parte, end=" ")

# E18

speed = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}

# Cria um conjunto para armazenar os valores únicos
valores_unicos = set(speed.values())

# Converte o conjunto de valores não repetem em uma lista
lista_valores_unicos = list(valores_unicos)

# imprime valores que não se repetem
print(lista_valores_unicos)

# E19

"""
import random

random_list = random.sample(range(500), 50)


mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0
"""
import random

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)

# Ordena a lista
random_list.sort()

# Calcula o valor mínimo
valor_minimo = random_list[0]

# Calcula o valor máximo
valor_maximo = random_list[-1]

# Calcula a média
media = sum(random_list) / len(random_list)

# Calcula a mediana
if len(random_list) % 2 == 0:
    mediana = (
        random_list[len(random_list) // 2] + random_list[len(random_list) // 2 - 1]
    ) / 2
else:
    mediana = random_list[len(random_list) // 2]

print(
    f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}"
)

# E20

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista_aocontrario = []
for i in range(len(a) - 1, -1, -1):
    lista_aocontrario.append(a[i])

print(lista_aocontrario)
