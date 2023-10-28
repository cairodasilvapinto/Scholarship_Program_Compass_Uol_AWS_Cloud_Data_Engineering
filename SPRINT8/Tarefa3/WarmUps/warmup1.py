import random

# declarando e inicializando a lista com 250 inteiros aleatórios
lista = [random.randint(0, 1000) for i in range(250)]

print("lista original: ", lista, "\n")

# aplicando o método reverse na lista
lista.reverse()

# imprimindo o resultado
print("lista revertida: ", lista)
