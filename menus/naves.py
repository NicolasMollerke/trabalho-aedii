def menu_naves(trie, lista, tipo):
    while True:
        print("\n---PESQUISA DE NAVES---")
        
        if tipo == "nome":
            nome = input("Digite o nome (ou '0' para voltar): ").strip()
            
            if nome == "0": 
                break
                
            resultado, nos = trie.buscar(nome)
                        
            if resultado: 
                resultado.exibir_detalhes()
                print(f"Nós Percorridos: {nos}")
            else: 
                print(f"\n[x] Não encontrado.")

        elif tipo == "atributo":
            print("\n[!] Pesquisa por atributos em desenvolvimento...")
            break
        elif tipo == "prefixo":
            prefixo = input("Digite o prefixo (ou '0' para voltar): ").strip()

            if prefixo == "0": 
                break

            resultado, nos = trie.buscaPrefixo(prefixo)

            if resultado:
                for r in resultado:
                    r.exibir_detalhes()
                print(f"Nós Percorridos: {nos}")
            else: 
                print(f"\n[x] Não encontrado.")