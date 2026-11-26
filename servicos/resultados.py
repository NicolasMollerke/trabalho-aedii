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

def exibir_rota(origem, destino, caminho, custo, visitados):
    print("\n" + "-" * 40)
    print("ROTA MAIS CURTA (Dijkstra)".center(40))
    print("-" * 40)

    if not caminho:
        print(f"[x] Não existe rota entre {origem.nome} e {destino.nome}.")
    else:
        nomes = [planeta.nome for planeta in caminho]
        print(f"Percurso: {' → '.join(nomes)}")
        print(f"Saltos: {len(caminho) - 1}")
        print(f"Distância total: {custo:.1f}")

    print(f"Planetas finalizados na busca: {visitados}")
    print("-" * 40)

def exibir_sequencia(final, bloqueados):
    print("\n" + "-" * 40)
    print("CRONOGRAMA DA MISSÃO (Kahn)".center(40))
    print("-" * 40)

    if not bloqueados:
        print("Sequência válida de execução:")
        for posicao, atividade in enumerate(final, start=1):
            print(f"  {posicao}. {atividade}")
    else:
        print("[x] Não existe sequência válida: há dependências circulares.")

        if final:
            print("\nAtividades que podem ser executadas:")
            for posicao, atividade in enumerate(final, start=1):
                print(f"  {posicao}. {atividade}")

        print("\nAtividades bloqueadas:")
        for atividade in bloqueados:
            print(f"  - {atividade}")

    print(f"\nAtividades processadas: {len(final)} de {len(final) + len(bloqueados)}")
    print("-" * 40)

def exibir_conexoes(rede, arestas, custo, alcancados):
    print("\n" + "-" * 50)
    print("REDE DE CONEXÕES DE MENOR CUSTO (Prim)".center(50))
    print("-" * 50)

    for origem, destino, peso in arestas:
        print(f"  {origem.nome} — {destino.nome}: {peso:.1f}")

    total_vertices = len(rede.vertices)
    custo_rede = sum(peso for v in rede.vertices for peso, _ in rede.vizinhos(v)) / 2

    print(f"\nLigações selecionadas: {len(arestas)}")
    print(f"Custo total da rede mínima: {custo:.1f}")
    print(f"Custo de usar todas as rotas: {custo_rede:.1f}")

    if custo_rede > 0:
        economia = (1 - custo / custo_rede) * 100
        print(f"Economia: {economia:.1f}%")

    if alcancados < total_vertices:
        print(f"\n[!] A rede não é conexa: apenas {alcancados} de {total_vertices} planetas foram conectados.")

    print("-" * 50)