from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo
from servicos.filtros import filtrar_personagens
from servicos.resultados import exibir_resultados


def menu_personagens(trie, hashs, arvores, tipo):
    print("\n---PESQUISA DE PERSONAGENS---")

    mapa_atributos = {
        "1": ("Planeta de Origem", "planeta_origem"),
        "2": ("Gênero", "genero"),
        "3": ("Ano de Nascimento", "nascimento"),
        "4": ("Espécie", "especies")
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
        resultado, texto = filtrar_personagens(arvores)
        if resultado is not None:
            exibir_resultados(resultado, texto)