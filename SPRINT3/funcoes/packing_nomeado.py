# **kwargs significa keyword arguments, é um dict
# que contém os argumentos nomeados passados para a função.
# os ** são utilizados para desempacotar o dict.
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f"{posicao} -> {piloto}")


if __name__ == "__main__":
    resultado_f1(primeiro="L. Hamilton", segundo="M. Verstappen", terceiro="S. Vettel")
