from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.filtros import filtrar_planetas
from servicos.resultados import exibir_resultados

def menu_planetas(trie, hashs, arvores, tipo):
    print("\n---PESQUISA DE PLANETAS---")

    nos = 0
        
    mapa_atributos = {
        "1": ("Clima", "clima"),
        "2": ("Terreno", "terreno")
    }

    if tipo == "nome":
        resultado, texto = pesquisa_nome(trie)
        if resultado is not None:
            exibir_resultados(resultado, texto)
    elif tipo == "atributo":
        resultado, texto = pesquisa_atributo(hashs, mapa_atributos)
        if resultado is not None:
            exibir_resultados(resultado, texto)
    elif tipo == "prefixo":
        resultado, texto = pesquisa_prefixo(trie)
        if resultado is not None:
            exibir_resultados(resultado, texto)
    elif tipo == "filtro":
        resultado, texto = filtrar_planetas(arvores)
        if resultado is not None:
            exibir_resultados(resultado, texto)