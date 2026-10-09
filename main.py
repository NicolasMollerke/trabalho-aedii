import requests
from models.planeta import Planeta
from models.personagem import Personagem
from models.especie import Especie
from models.nave import Nave
from models.veiculo import Veiculo
from estruturas.trie import Trie
from menus.principal import exibir_menu_principal


def fetch_data(endpoint) -> list:
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

def cria_objetos(dados, classe) -> list:
    lista_objetos = []

    for d in dados:
        objeto = classe.criar(d)
        lista_objetos.append(objeto)

    return lista_objetos

def carregar_entidades_api():
    lista_planetas = cria_objetos(fetch_data("planets"), Planeta)
    lista_personagens = cria_objetos(fetch_data("people"), Personagem)
    lista_especies = cria_objetos(fetch_data("species"), Especie)
    lista_naves = cria_objetos(fetch_data("starships"), Nave)
    lista_veiculos = cria_objetos(fetch_data("vehicles"), Veiculo)
    
    return lista_planetas, lista_personagens, lista_especies, lista_naves, lista_veiculos

def cruzar_dados(lista_origem, lista_destino, ids, destino):
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

def estabelecer_relacionamentos(planetas, personagens, especies, naves, veiculos):
    cruzar_dados(personagens, especies, "especies_ids", "especies")
    cruzar_dados(personagens, planetas, "planeta_origem_id", "planeta_origem")
    cruzar_dados(personagens, naves, "naves_ids", "naves")
    cruzar_dados(personagens, veiculos, "veiculos_ids", "veiculos")

    cruzar_dados(especies, personagens, "personagens_ids", "personagens")
    cruzar_dados(planetas, personagens, "residentes_ids", "residentes")
    cruzar_dados(naves, personagens, "pilotos_ids", "pilotos")
    cruzar_dados(veiculos, personagens, "pilotos_ids", "pilotos")

def inicializar_tries(planetas, personagens, especies, naves, veiculos):
    tries = {
        "planetas": Trie(),
        "personagens": Trie(),
        "especies": Trie(),
        "naves": Trie(),
        "veiculos": Trie()
    }
    
    inserir_trie(planetas, tries["planetas"])
    inserir_trie(personagens, tries["personagens"])
    inserir_trie(especies, tries["especies"])
    inserir_trie(naves, tries["naves"])
    inserir_trie(veiculos, tries["veiculos"])
    
    return tries

def inserir_trie(lista, trie):
    for i in lista:
        trie.inserir(i.nome, i)


def main():
    planetas, personagens, especies, naves, veiculos = carregar_entidades_api()
    
    estabelecer_relacionamentos(planetas, personagens, especies, naves, veiculos)
    
    tries = inicializar_tries(planetas, personagens, especies, naves, veiculos)

    conjuntos = {
        "planetas": {"trie": tries["planetas"], "lista": planetas},
        "personagens": {"trie": tries["personagens"], "lista": personagens},
        "especies": {"trie": tries["especies"], "lista": especies},
        "naves": {"trie": tries["naves"], "lista": naves},
        "veiculos": {"trie": tries["veiculos"], "lista": veiculos}
    }

    exibir_menu_principal(conjuntos)   


if __name__ == "__main__":
    main()