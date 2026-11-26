import heapq
from collections import deque

from estruturas.hash import TabelaHash

class Grafo:
    def __init__(self, direcionado=False):
        self.adjacencias = TabelaHash()
        self.vertices = []
        self.direcionado = direcionado

    def existe_aresta(self, a, b):
        viz = self.vizinhos(a)

        for peso, vizinho in viz:
            if b == vizinho:
                return True

        return False

    def inserir_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

    def inserir_aresta(self, a, b, peso=0):
        if not self.existe_aresta(a, b):
            self.adjacencias.inserir(a, (peso, b))

            if not self.direcionado:
                self.adjacencias.inserir(b, (peso, a))

            self.inserir_vertice(a)
            self.inserir_vertice(b)

    def vizinhos(self, v):
        resultado = self.adjacencias.buscar(v)

        if resultado: 
            return resultado

        return []

    def dijkstra(self, origem, destino):
        distancia = {p: float("inf") for p in self.vertices}
        anterior = {}
        finalizadas = set()

        if origem not in self.vertices or destino not in self.vertices:
            return [], float("inf"), len(finalizadas)
        
        distancia[origem] = 0
        fila = [(0, 0, origem)]

        contador = 0

        while fila:
            d, _, atual = heapq.heappop(fila)
            if atual in finalizadas:
                continue
            finalizadas.add(atual)

            if atual == destino:
                break

            for peso, vizinho in self.vizinhos(atual):
                if vizinho in finalizadas:
                    continue
                nova = d + peso
                if nova < distancia[vizinho]:
                    distancia[vizinho] = nova
                    anterior[vizinho] = atual
                    contador += 1
                    heapq.heappush(fila, (nova, contador, vizinho))


        if distancia[destino] == float("inf"):
            return [], float("inf"), len(finalizadas)

        caminho = [destino]
        while caminho[-1] != origem:
            caminho.append(anterior[caminho[-1]])
        caminho.reverse()

        return caminho, distancia[destino], len(finalizadas)

    def graus_entrada(self):
        contador = {p: 0 for p in self.vertices}

        for v in self.vertices:
            vizinhos = self.vizinhos(v)

            for peso, vertice in vizinhos:
                contador[vertice] += 1

        return contador

    def kahn(self):
        contador = self.graus_entrada()

        fila = deque()

        final = []
        bloqueados = []

        for vertice, grau in contador.items():
            if grau == 0:   
                fila.append(vertice)

        while fila:
            atual = fila.popleft()

            final.append(atual)

            vizinhos = self.vizinhos(atual)

            for peso, vizinho in vizinhos:
                contador[vizinho] -= 1

                if contador[vizinho] == 0:
                    fila.append(vizinho)

        for v in self.vertices:
            if contador[v] > 0:
                bloqueados.append(v)

        return final, bloqueados

    def prim(self):
        if not self.vertices:
            return [], 0, 0

        inicio = self.vertices[0]
        
        distancia = {p: float("inf") for p in self.vertices}
        anterior = {}
        finalizadas = set()

        distancia[inicio] = 0
        fila = [(0, 0, inicio)]

        contador = 0
        arestas = []
        custo = 0

        while fila:
            d, _, atual = heapq.heappop(fila)
            if atual in finalizadas:
                continue
            finalizadas.add(atual)

            if atual in anterior:
                arestas.append((anterior[atual], atual, d))
                custo += d

            for peso, vizinho in self.vizinhos(atual):
                if vizinho in finalizadas:
                    continue

                if peso < distancia[vizinho]:
                    distancia[vizinho] = peso
                    anterior[vizinho] = atual
                    contador += 1
                    heapq.heappush(fila, (peso, contador, vizinho))

        return arestas, custo, len(finalizadas)

    


        
        