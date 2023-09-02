import hashlib

while True:
    entrada = input("Digite algo para ser mascarado (ou sair para encerrar): ")
    if entrada.lower() == "sair":
        break

    print(hashlib.sha1(entrada.encode()).hexdigest())
