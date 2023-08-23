class Potencia:
    # Calcula a potencia especificada
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base**self.expoente


if __name__ == "__main__":
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f"3² => {quadrado(3)}")
        print(f"5³ => {cubo(5)}")
        print(Potencia(4)(2))
