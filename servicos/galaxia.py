import random
import math
from estruturas.grafo import Grafo

def montar_grafo(planetas, k=3, semente=42):
    filtrados = []

    for p in planetas:
        if p.nome == "unknown":
            continue

        filtrados.append(p)
    
    gerar_coordenadas(filtrados, semente)

    grafo = Grafo()

    ligacoes(filtrados, grafo, k)

    return grafo
    

def gerar_coordenadas(planetas, semente):
    random.seed(semente)                  
    
    for p in planetas:
        p.x = random.uniform(0, 1000)     
        p.y = random.uniform(0, 1000)  

def ligacoes(planetas, grafo, k):
    for p in planetas:
        candidatos = []
        
        for p2 in planetas:
            if p2 == p:
                continue
            d = distancia(p, p2)

            candidatos.append([d, p2])

        candidatos.sort(key=lambda par: par[0])

        for d, vizinho in candidatos[:k]:
            grafo.inserir_aresta(p, vizinho, d)

def distancia(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)