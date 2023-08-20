with open(
    "pessoas.csv"
) as arquivo:  # with é uma forma mais elegante de se trabalhar com arquivos
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("Arquivo já foi fechado")
