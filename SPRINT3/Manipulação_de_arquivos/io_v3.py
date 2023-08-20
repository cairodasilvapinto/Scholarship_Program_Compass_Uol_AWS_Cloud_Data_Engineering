arquivo = open("pessoas.csv")
for registro in arquivo:  # streaming
    print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))
arquivo.close()  # strip() remove espaços em branco
