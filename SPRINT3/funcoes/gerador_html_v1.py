def tag_bloco(conteudo, classe="success"):
    return f'<div class="{classe}">{conteudo}</div>'


if __name__ == "__main__":
    # Testes (assertions)
    assert (
        tag_bloco("Incluído com sucesso!")
        == '<div class="success">Incluído com sucesso!</div>'
    )
    assert (
        tag_bloco("Impossível excluir!", "error")
        == '<div class="error">Impossível excluir!</div>'
    )
    print(tag_bloco("bloco"))
