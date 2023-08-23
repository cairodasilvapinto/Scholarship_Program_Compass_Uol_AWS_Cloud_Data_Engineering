# existem dois tipos de parametros: posicionais e nomeados
def todos_parametos(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if __name__ == "__main__":
    # parametros posicionais(args)
    # parametros nomeados(kwargs)
    todos_parametos("a", "b", "c")
    todos_parametos(1, 2, 3, legal=True, valor=12.99)
    todos_parametos("Ana", False, [1, 2, 3], tamanho="M", fragil=False)
    todos_parametos(primeiro="João", segundo="Maria")
    todos_parametos("Maria", primeiro="João")
