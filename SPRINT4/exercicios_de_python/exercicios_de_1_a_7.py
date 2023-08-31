# E1

# Função para verificar se um número é par
epar = lambda x: x % 2 == 0

# Lê os números do arquivo e filtra os pares
with open("number.txt", "r") as file:
    num = map(int, file.readlines())
    par_num = filter(epar, num)

# Ordena os números pares em ordem decrescente
sorted_par_num = sorted(par_num, reverse=True)

# Pega os 5 maiores números pares
top_5_par_num = sorted_par_num[:5]

# Calcula a soma dos 5 maiores números pares
sum_top_5 = sum(top_5_par_num)

# Exibe os resultados
print(top_5_par_num)
print(sum_top_5)


# E2


# Define uma função chamada conta_vogais.
# texto: str indica que a função espera um parâmetro chamado 'texto',
# que deve ser uma string.
# O -> int indica que a função retorna um valor inteiro.
def conta_vogais(texto: str) -> int:
    # Função lambda para verificar se um caractere é uma vogal
    evogal = lambda char: char.lower() in "aeiou"

    # Filtra as vogais do texto
    vogal = filter(evogal, texto)

    # Conta o número de vogais usando a função len
    conta_vogal = len(list(vogal))

    return conta_vogal


texto = "Hello World"
print(conta_vogais(texto))

# E3

from functools import reduce

lancamentos = [(200, "D"), (300, "C"), (100, "C")]


# Definindo a função calcula_saldo com anotação de tipo
def calcula_saldo(lancamentos) -> float:
    # Usando map para transformar cada tupla em um valor numérico
    # Se o tipo for 'C', o valor é positivo, se for 'D', o valor é negativo
    valores = map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos)
    # Usando reduce para somar todos os valores e obter o saldo final
    saldo = reduce(lambda x, y: x + y, valores)
    # Retornando o saldo como float
    return float(saldo)


# Testando a função com a lista de lançamentos
print(calcula_saldo(lancamentos))


lancamentos = [(200, "D"), (300, "C"), (100, "C")]


print(calcula_saldo(lancamentos))

# E4

operadores = ["+", "-", "*", "/", "+"]

operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

operacoes = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "%": lambda x, y: x % y,
}


# Definindo a função calcular_valor_maximo com anotação de tipo
def calcular_valor_maximo(operadores, operandos) -> float:
    # Usando zip para criar um iterável que combina os operadores e os operandos
    combinacoes = zip(operadores, operandos)
    # Usando map para aplicar cada operador ao respectivo par de operandos
    resultados = map(lambda x: operacoes[x[0]](*x[1]), combinacoes)
    # Usando max para obter o maior valor entre os resultados
    valor_maximo = max(resultados)
    # Retornando o valor máximo como float
    return float(valor_maximo)


print(calcular_valor_maximo(operadores, operandos))

# E5

import csv


# Função para formatar a média conforme o pedido
def formatar_media(media):
    formatted = "{:.2f}".format(media)
    if formatted[-1] == "0" and formatted[-2] == "0":
        return formatted[:-1]
    return formatted


with open("estudantes.csv", newline="") as csvfile:
    # Criar um objeto reader que vai iterar sobre as linhas do arquivo
    reader = csv.reader(csvfile)
    # Criar uma lista vazia para armazenar os dados processados
    data = []
    for row in list(reader)[0:]:
        nome = row[0]
        # Obter as cinco notas como números reais
        notas = list(map(float, row[1:]))
        # Ordenar as notas em ordem decrescente
        maiores = sorted(notas, reverse=True)[:3]
        # Calcular a média das três maiores notas com duas casas decimais de precisão
        media = round(sum(maiores) / 3, 2)
        # Adicionar o nome, as maiores notas e a média à lista de dados
        data.append((nome, maiores, media))
    # Ordenar os dados pelo nome do estudante
    data.sort()
    for nome, maiores, media in data:
        # Formata a média conforme a função definida
        formatted_media = formatar_media(media)
        print(
            f"Nome: {nome} Notas: {[int(nota) for nota in maiores]} Média: {formatted_media}"
        )

# E6


def maiores_que_media(conteudo: dict) -> list:
    # Calcular a média dos valores dos produtos
    media = sum(conteudo.values()) / len(conteudo)

    # Usar list comprehension para filtrar os produtos com preço acima da média
    produtos_acima_media = [
        (produto, preco) for produto, preco in conteudo.items() if preco > media
    ]

    # Ordenar a lista de produtos acima da média pelo preço
    produtos_acima_media.sort(key=lambda x: x[1])

    return produtos_acima_media


# E7


def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i


for par in pares_ate(10):
    print(par)

# assim também vai:
# valores_pares = list(pares_ate(10))
# print(valores_pares)
