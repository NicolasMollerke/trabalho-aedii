import requests
from models.planeta import Planeta
from models.personagem import Personagem
from models.especie import Especie
from models.nave import Nave
from models.veiculo import Veiculo
from estruturas.trie import Trie


def fetch_data(endpoint: str) -> list:
    """
    Realiza requisições sucessivas à SWAPI acompanhando o link 'next' 
    até consumir todas as páginas do recurso solicitado.
    """
    url_atual = f"https://swapi.dev/api/{endpoint}/"
    resultados = []

    while url_atual:
        response = requests.get(url_atual)

        if response.status_code == 200:
            dados_pagina = response.json()
            
            resultados_pagina = dados_pagina.get("results", [])
            
            resultados.extend(resultados_pagina)
            
            url_atual = dados_pagina.get("next")
        else:
            break

    return resultados

def cria_objetos(dados: list, classe: type) -> list:
    lista_objetos = []

    for d in dados:
        objeto = classe.criar(d)
        lista_objetos.append(objeto)

    return lista_objetos

def cruzar_dados(lista_origem: list, lista_destino: list, ids: str, destino: str):
    mapa_destino = {item.id: item for item in lista_destino}

    for item in lista_origem:
        valor_id = getattr(item, ids, None)

        if valor_id is None:
            continue

        if isinstance(valor_id, int): #destino é um valor unico como planeta_origem
            objeto_encontrado = mapa_destino.get(valor_id)
            setattr(item, destino, objeto_encontrado)

        elif isinstance(valor_id, list): #destino é uma lista como residentes
            objetos_cruzados = [mapa_destino[i] for i in valor_id if i in mapa_destino]
            setattr(item, destino, objetos_cruzados)

def inserir_trie(lista: list, trie: Trie):
    for i in lista:
        trie.inserir(i.nome, i)


def main():
    planetas = fetch_data("planets")
    lista_planetas = cria_objetos(planetas, Planeta)

    personagens = fetch_data("people")
    lista_personagens = cria_objetos(personagens, Personagem)

    especies = fetch_data("species")
    lista_especies = cria_objetos(especies, Especie)

    naves = fetch_data("starships")
    lista_naves = cria_objetos(naves, Nave)

    veiculos = fetch_data("vehicles")
    lista_veiculos = cria_objetos(veiculos, Veiculo)

    cruzar_dados(lista_personagens, lista_especies, "especies_ids", "especies")
    cruzar_dados(lista_personagens, lista_planetas, "planeta_origem_id", "planeta_origem")
    cruzar_dados(lista_personagens, lista_naves, "naves_ids", "naves")
    cruzar_dados(lista_personagens, lista_veiculos, "veiculos_ids", "veiculos")

    cruzar_dados(lista_especies, lista_personagens, "personagens.ids", "personagens")

    cruzar_dados(lista_planetas, lista_personagens, "residentes.ids", "residentes")

    cruzar_dados(lista_naves, lista_personagens, "pilotos.ids", "pilotos")

    cruzar_dados(lista_veiculos, lista_personagens, "pilotos.ids", "pilotos")

    trie_planetas = Trie()
    inserir_trie(lista_planetas, trie_planetas)

    tatooine = trie_planetas.buscar("tatooine")
    print(tatooine)

    


if __name__ == "__main__":
    main()