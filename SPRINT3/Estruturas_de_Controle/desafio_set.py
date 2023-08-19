PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
textos = [
    "João gosta de futebol e política",
    "A praia foi divertida",
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Texto possui pelo menos uma palavra proibida:", intersecao)
    else:
        print("Texto autorizado:", texto)
