try:
    arquivo = open("pessoas.csv")

    for registro in arquivo:  # streaming # strip() remove espaços em branco
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))
except IndexError:
    pass
finally:
    # finally é executado independente de erro ou não
    print("Finally")
    arquivo.close()

if arquivo.closed:
    print("Arquivo já foi fechado")
