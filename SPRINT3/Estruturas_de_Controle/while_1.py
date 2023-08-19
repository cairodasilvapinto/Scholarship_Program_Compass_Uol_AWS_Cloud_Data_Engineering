# while True:
#    print("vai demorar muitooooo")

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

# while é recomendado quando não se sabe quantas vezes o loop será executado
while numero_informado != numero_secreto:
    numero_informado = int(input("Informe o número: "))

print("Número secreto {} foi encontrado!".format(numero_secreto))
