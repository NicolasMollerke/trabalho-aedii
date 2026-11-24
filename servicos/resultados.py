def exibir_resultados(resultado, texto):
    if resultado:
        if isinstance(resultado, list):
            for r in resultado:
                r.exibir_detalhes()
        else:
            resultado.exibir_detalhes()
            
        print(texto)

    else: 
        print(f"\n[x] Não encontrado.")
