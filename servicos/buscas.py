def pesquisa_nome(trie):
    nome = input("Digite o nome (ou '0' para voltar): ").strip()
            
    if nome == "0": 
        return 0
                
    resultado, nos = trie.buscar(nome)

    return resultado, nos

def pesquisa_atributo(lista, mapa_atributos):
    resultados = []

    for chave, atributo in mapa_atributos.items():
        print(f"[{chave}] {atributo[0]}")
    
    opcao = input("Digite o atributo (ou '0' para voltar): ").strip()

    if opcao == "0": 
        return 0

    if opcao in mapa_atributos:
        termo = input(f"O que você deseja aprocurar em {mapa_atributos[opcao][0]}: ").lower()
        atributo_escolhido = mapa_atributos[opcao][1]

        for l in lista:
            atributo = getattr(l, atributo_escolhido)
        
            if isinstance(atributo, list):
                for item in atributo:
                    nome_item = str(getattr(item, "nome", item)).lower()
                    if termo in nome_item:
                        resultados.append(l)
                        break
            else:
                if termo in str(atributo).lower():
                    resultados.append(l)

        return resultados
    else:
        print("\n[x] Opção inválida.")

def pesquisa_prefixo(trie):
    prefixo = input("Digite o prefixo (ou '0' para voltar): ").strip()

    if prefixo == "0": 
        return 0
    resultado, nos = trie.busca_prefixo(prefixo)
    
    return resultado, nos



