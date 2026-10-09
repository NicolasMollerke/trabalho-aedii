from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.filtros import filtrar_planetas
from servicos.resultados import exibir_resultados

def menu_planetas(trie, lista, tipo):
    print("\n---PESQUISA DE PLANETAS---")

    nos = 0
        
    mapa_atributos = {
        "1": ("Clima", "clima"),
        "2": ("Terreno", "terreno")
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
        resultado = filtrar_planetas(lista)
        if resultado is not None:
            exibir_resultados(resultado)
