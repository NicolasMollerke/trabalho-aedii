from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.resultados import exibir_resultados
from servicos.filtros import filtrar_naves


def menu_naves(trie, hashs, tipo):
    print("\n---PESQUISA DE NAVES---")

    nos = 0
        
    mapa_atributos = {
        "1": ("Classe", "classe_nave"),
        "2": ("Fabricante", "fabricante")
    }

    if tipo == "nome":
        resultado, nos = pesquisa_nome(trie)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "atributo":
        resultado = pesquisa_atributo(hashs, mapa_atributos)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "prefixo":
        resultado, nos = pesquisa_prefixo(trie)
        if resultado is not None:
            exibir_resultados(resultado, nos)
    elif tipo == "filtro":
        resultado = filtrar_naves(hashs)
        if resultado is not None:
            exibir_resultados(resultado)