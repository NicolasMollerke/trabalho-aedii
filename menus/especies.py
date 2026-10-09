from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.resultados import exibir_resultados
from servicos.filtros import filtrar_especies

def menu_especies(trie, lista, tipo):
    print("\n---PESQUISA DE ESPÉCIES---")

    nos = 0
    mapa_atributos = {
        "1": ("Classificação", "classificacao"),
        "2": ("Planeta de Origem", "planeta_origem"),
        "3": ("Linguagem", "idioma")
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
    elif tipo == "prefixo":
        resultado = pesquisa_prefixo(trie)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "filtro":
        resultado = filtrar_especies(lista)
        if resultado is not None:
            exibir_resultados(resultado)
