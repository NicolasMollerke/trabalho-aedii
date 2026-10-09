from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.filtros import filtrar_personagens
from servicos.resultados import exibir_resultados


def menu_personagens(trie, lista, tipo):
    print("\n---PESQUISA DE PERSONAGENS---")

    nos = 0

    mapa_atributos = {
        "1": ("Planeta de Origem", "planeta_origem"),
        "2": ("Gênero", "genero"),
        "3": ("Ano de Nascimento", "nascimento"),
        "4": ("Espécie", "especies")
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
    elif tipo == "filtro":
        resultado = filtrar_personagens(lista)
        if resultado is not None:
            exibir_resultados(resultado)