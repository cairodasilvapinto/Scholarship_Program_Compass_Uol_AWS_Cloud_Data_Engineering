# lista de animais
animais = [
    "ornitorrinco",
    "peixe-boi",
    "dragao-de-komodo",
    "toupeira-estrela",
    "morcego-nariz-de-porco",
    "panda-vermelho",
    "mico-leao-dourado",
    "gato-do-deserto",
    "gato-de-pallas",
    "gato-de-areia",
    "gato-de-geoffroy",
    "gato-de-temminck",
    "gato-de-iroques",
    "gato-de-pallas",
    "gato-de-bay",
    "gato-de-manchas",
    "gato-de-pescador",
    "gato-de-cabeca-chata",
    "gato-de-orelhas-pretas",
    "gato-de-patas-negras",
    "ornitorrinco-de-bico-largo",
    "peixe-boi-da-amazonia",
    "dragao-de-komodo-de-garganta-rosa",
    "toupeira-estrela-de-olhos-azuis",
    "morcego-nariz-de-porco-de-orelhas-grandes",
    "panda-vermelho-de-cauda-longa",
    "mico-leao-dourado-de-crista-alta",
    "gato-do-deserto-de-olhos-azuis",
    "gato-de-pallas-de-pelagem-longa",
    "gato-de-areia-de-olhos-vermelhos",
    "gato-de-geoffroy-de-cauda-curta",
    "gato-de-temminck-de-orelhas-pontudas",
    "gato-de-iroques-de-pelagem-azul",
    "gato-de-pallas-de-olhos-verdes",
    "gato-de-bay-de-pelagem-rosa",
    "gato-de-manchas-de-olhos-amarelos",
    "gato-de-pescador-de-pelagem-cinza",
    "gato-de-cabeca-chata-de-olhos-vermelhos",
    "gato-de-orelhas-pretas-de-pelagem-branca",
    "gato-de-patas-negras-de-olhos-azuis",
]

# ordena a lista em ordem crescente
animais.sort()

# itera sobre os itens e imprime um a um
[print(animal) for animal in animais]

# armazena o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV
with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")
