from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.resultados import exibir_resultados
from servicos.filtros import filtrar_naves


def menu_naves(trie, hashs, arvores, tipo):
    print("\n---PESQUISA DE NAVES---")
        
    mapa_atributos = {
        "1": ("Classe", "classe_nave"),
        "2": ("Fabricante", "fabricante")
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
        resultado, texto = filtrar_naves(arvores)
        if resultado is not None:
            exibir_resultados(resultado, texto)