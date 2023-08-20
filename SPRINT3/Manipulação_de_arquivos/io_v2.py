arquivo = open("pessoas.csv")
for registro in arquivo:  # streaming
    print("Nome: {}, Idade: {}".format(*registro.split(",")))
arquivo.close()
