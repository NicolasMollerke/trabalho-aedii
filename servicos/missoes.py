from estruturas.grafo import Grafo

ATIVIDADES = [
    "Contatar a Aliança em Yavin 4",
    "Recrutar piloto",
    "Reabastecer a nave",
    "Obter os planos da Estrela da Morte",
    "Preparar o X-wing",
    "Planejar o ataque",
    "Atacar a Estrela da Morte",
]

DEPENDENCIAS = [
    ("Contatar a Aliança em Yavin 4", "Recrutar piloto"),
    ("Recrutar piloto", "Preparar o X-wing"),
    ("Reabastecer a nave", "Preparar o X-wing"),
    ("Obter os planos da Estrela da Morte", "Planejar o ataque"),
    ("Contatar a Aliança em Yavin 4", "Planejar o ataque"),
    ("Preparar o X-wing", "Atacar a Estrela da Morte"),
    ("Planejar o ataque", "Atacar a Estrela da Morte"),
]

def montar_missao():
    grafo = Grafo(True)

    for a in ATIVIDADES:
        grafo.inserir_vertice(a)

    for antes, depois in DEPENDENCIAS:
        grafo.inserir_aresta(antes, depois)

    return grafo