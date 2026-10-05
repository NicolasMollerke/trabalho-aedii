from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo, exibir_resultados

def menu_veiculos(trie, lista, tipo):
    print("\n---PESQUISA DE VEÍCULOS---")

    nos = 0
        
    mapa_atributos = {
        "1": ("Classe", "classe_veiculo"),
        "2": ("Modelo", "modelo")
    }

    if tipo == "nome":
        resultado, nos = pesquisa_nome(trie)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "atributo":
        resultado = pesquisa_atributo(lista, mapa_atributos)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "prefixo":
        resultado, nos = pesquisa_prefixo(trie)
        if resultado is not None:
            exibir_resultados(resultado, nos)
