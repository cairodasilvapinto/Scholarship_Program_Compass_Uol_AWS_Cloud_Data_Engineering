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
        if dia == 1 and dia == 7:
            print(f"{dia}: {get_dia_semana(dia)} - Fim de semana")
        else:
            print(f"{dia}: {get_dia_semana(dia)} - Dia útil")


# Versão da Aula
def get_dia_semana(dia):
    dias = {
        1: "Fim de semana",
        2: "Dia útil",
        3: "Dia útil",
        4: "Dia útil",
        5: "Dia útil",
        6: "Dia útil",
        7: "Fim de semana",
    }
    return dias.get(dia, "** inválido **")


if __name__ == "__main__":
    for dia in range(8):
        print(f"{dia}: {get_dia_semana(dia)}")
