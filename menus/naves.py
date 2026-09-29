from servicos.buscas import pesquisa_prefixo, pesquisa_nome, pesquisa_atributo, exibir_resultados

def menu_naves(trie, lista, tipo):
    while True:
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
