# E1


import datetime

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano = datetime.datetime.now().year
print(ano + (100 - idade))

# E2


def verifica_par(n):
    if n % 2 == 0:
        return "Par:"
    else:
        return "Ímpar:"


for i in range(3):
    n = int(input())
    print(verifica_par(n), n)

# E3
for i in range(0, 21, 2):
    print(i)


# E4
def verifica_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 101):
    if verifica_primo(i):
        print(i)


# E5

dia = 22
mes = 10
ano = 2022
print(f"{dia}/{mes}/{ano}")
