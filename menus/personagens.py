from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo, exibir_resultados

def menu_personagens(trie, lista, tipo):
    while True:
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
            break
        elif tipo == "atributo":
            resultado = pesquisa_atributo(lista, mapa_atributos)
            if resultado is not None:
                exibir_resultados(resultado, nos)
            break
        elif tipo == "prefixo":
            resultado, nos = pesquisa_prefixo(trie)
            if resultado is not None:
                exibir_resultados(resultado, nos)
            break
