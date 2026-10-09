def exibir_resultados(resultado, nos=None):
    if resultado:
        if isinstance(resultado, list):
            for r in resultado:
                r.exibir_detalhes()
        else:
            resultado.exibir_detalhes()
        if nos is not None:
            print(f"Nós percorridos: {nos}")

    else: 
        print(f"\n[x] Não encontrado.")
