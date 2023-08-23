# E21
class Passaro:
    def __init__(self):
        self.voa = True
        self.emite_som = True

    def voar(self):
        if self.voa:
            print("Voando...")
        else:
            print("Não consigo voar.")

    def emitir_som(self):
        if self.emite_som:
            print("Emitindo som...")
        else:
            print("Não consigo emitir som.")


class Pato(Passaro):
    def __init__(self):
        super().__init__()
        self.emite_som = "Quack Quack"


class Pardal(Passaro):
    def __init__(self):
        super().__init__()
        self.emite_som = "Piu Piu"


if __name__ == "__main__":
    pato = Pato()
    pato.voar()
    pato.emitir_som()

    pardal = Pardal()
    pardal.voar()
    pardal.emitir_som()


# E22
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == "__main__":
    pessoa = Pessoa(0)
    pessoa.nome = "Fulano De Tal"
    print(pessoa.nome)

# E23


class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self):
        return self.x + self.y

    def subtracao(self):
        return self.x - self.y


if __name__ == "__main__":
    calculo = Calculo(4, 5)
    print("Somando:", calculo.soma())
    print("Subtraindo:", calculo.subtracao())

# E24


class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)


crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())

# E25


class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"


avioes = []

# Definindo os valores diretamente no código
modelo_1, velocidade_maxima_1, capacidade_1 = (
    "BOIENG456",
    "1500 km/h",
    "400 passageiros",
)
modelo_2, velocidade_maxima_2, capacidade_2 = (
    "Embraer Praetor 600",
    "863 km/h",
    "14 passageiros",
)
modelo_3, velocidade_maxima_3, capacidade_3 = (
    "Antonov An-2",
    "258 km/h",
    "12 passageiros",
)

# Criando os objetos da classe Avião
avioes.append(Aviao(modelo_1, velocidade_maxima_1, capacidade_1))
avioes.append(Aviao(modelo_2, velocidade_maxima_2, capacidade_2))
avioes.append(Aviao(modelo_3, velocidade_maxima_3, capacidade_3))

# Iterando pela lista e imprimindo os objetos
for avio in avioes:
    print(
        f"O avião de modelo {avio.modelo} possui uma velocidade máxima de {avio.velocidade_maxima}, capacidade para {avio.capacidade} e é da cor {avio.cor}."
    )
