# for i in range(1, 11):
#    if i == 6:
#        break
#    print(i)
# else:
#    print("Fim!")

# Funcao sortear_dado numeros entre 1  a 6
# For com range de 1 a 6
# se for impar continue
# se o numeor for par e for igual ao valor sorteado pela funcao dado imprimir "ACERTOU" e depois chamar o break
# Senão acertar chama o else... print("Não acertou o número")


def sortear_dado():
    from random import randint

    return randint(1, 6)


for i in range(1, 7):
    if i % 2 != 0:
        continue
    elif i == sortear_dado():
        print("ACERTOU", i)
        break
else:
    print("Não acertou o número")
