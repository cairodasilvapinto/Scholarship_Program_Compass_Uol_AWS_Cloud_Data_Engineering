# Em python não existe switch,
# mas podemos usar uma função e um dicionário para simular o mesmo resultado.
def get_dia_semana(dia):
    dias = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado",
    }
    return dias.get(dia, "** inválido **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_dia_semana(dia)}")
