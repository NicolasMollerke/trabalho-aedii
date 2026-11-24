from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.resultados import exibir_resultados
from servicos.filtros import filtrar_especies

def menu_especies(trie, hashs, arvores, tipo):
    print("\n---PESQUISA DE ESPÉCIES---")

    nos = 0
    mapa_atributos = {
        "1": ("Classificação", "classificacao"),
        "2": ("Planeta de Origem", "planeta_origem"),
        "3": ("Linguagem", "idioma")
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
        resultado, texto = filtrar_especies(arvores)
        if resultado is not None:
            exibir_resultados(resultado, texto)
