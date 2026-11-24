def pesquisa_nome(trie):
    nome = input("Digite o nome (ou '0' para voltar): ").strip()
            
    if nome == "0": 
        return 0
                
    resultado, nos = trie.buscar(nome)

    texto = f"Nós percorridos: {trie.nos_visitados}"

    return resultado, texto

def pesquisa_atributo(hashs, mapa_atributos):
    resultados = []

    for chave, atributo in mapa_atributos.items():
        print(f"[{chave}] {atributo[0]}")
    
    opcao = input("Digite o atributo (ou '0' para voltar): ").strip()

    if opcao == "0": 
        return None, None

    if opcao in mapa_atributos:
        termo = input(f"O que você deseja aprocurar em {mapa_atributos[opcao][0]}: ").strip().lower()
        atributo_escolhido = mapa_atributos[opcao][1]

        tabela = hashs[atributo_escolhido]

        resultados = tabela.buscar(termo)

        texto = f"Colisões: {tabela.colisoes} | Fator de Carga: {tabela.fator_carga():.2f}"

        return resultados, texto
    else:
        print("\n[x] Opção inválida.")
        return None, None

def pesquisa_prefixo(trie):
    prefixo = input("Digite o prefixo (ou '0' para voltar): ").strip()

    if prefixo == "0": 
        return 0
    resultado, nos = trie.busca_prefixo(prefixo)

    texto = f"Nós percorridos: {trie.nos_visitados}"

    
    return resultado, texto



