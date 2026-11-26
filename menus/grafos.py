from servicos.resultados import exibir_rota, exibir_sequencia, exibir_conexoes 

def ler_planeta(grafo, mensagem):
    while True:
        nome = input(mensagem).strip().lower()

        if nome == "0":
            return None

        for planeta in grafo.vertices:
            if planeta.nome.lower() == nome:
                return planeta

        print("[x] Planeta não encontrado na rede. Tente novamente (ou '0' para voltar).")

def menu_grafos(grafos):
    while True:
        print("\n" + "="*40)
        print("[1] Caminho mínimo entre planetas")
        print("[2] Sequência de atividades")
        print("[3] Rede de conexões de menor custo")
        print("[0] Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            rede = grafos["planetas"]

            origem = ler_planeta(rede, "Digite o planeta de origem (ou '0' para voltar): ")
            if origem is None:
                continue

            destino = ler_planeta(rede, "Digite o planeta de destino (ou '0' para voltar): ")
            if destino is None:
                continue

            caminho, custo, visitados = rede.dijkstra(origem, destino)
            exibir_rota(origem, destino, caminho, custo, visitados)
        elif opcao == "2":
            missao = grafos["missao"]

            final, bloqueado = missao.kahn()
            exibir_sequencia(final, bloqueado)
        elif opcao == "3":
            rede = grafos["planetas"]

            arestas, custo, alcancados = rede.prim()
            exibir_conexoes(rede, arestas, custo, alcancados)
        elif opcao == "0":
            print("\nEncerrando o sistema. Que a Força esteja com você!")
            break
        else:
            print("\n[x] Opção inválida! Tente novamente.")