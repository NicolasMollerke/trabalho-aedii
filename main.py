import requests
from models.planeta import Planeta
from models.personagem import Personagem
from models.especie import Especie
from models.nave import Nave
from models.veiculo import Veiculo
from estruturas.trie import Trie
from estruturas.hash import TabelaHash
from menus.principal import exibir_menu_principal


def fetch_data(endpoint: str) -> list:
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

def carregar_entidades_api():
    lista_planetas = cria_objetos(fetch_data("planets"), Planeta)
    lista_personagens = cria_objetos(fetch_data("people"), Personagem)
    lista_especies = cria_objetos(fetch_data("species"), Especie)
    lista_naves = cria_objetos(fetch_data("starships"), Nave)
    lista_veiculos = cria_objetos(fetch_data("vehicles"), Veiculo)
    
    return lista_planetas, lista_personagens, lista_especies, lista_naves, lista_veiculos

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

def estabelecer_relacionamentos(planetas, personagens, especies, naves, veiculos):
    cruzar_dados(personagens, especies, "especies_ids", "especies")
    cruzar_dados(personagens, planetas, "planeta_origem_id", "planeta_origem")
    cruzar_dados(personagens, naves, "naves_ids", "naves")
    cruzar_dados(personagens, veiculos, "veiculos_ids", "veiculos")

    cruzar_dados(especies, personagens, "personagens_ids", "personagens")
    cruzar_dados(planetas, personagens, "residentes_ids", "residentes")
    cruzar_dados(naves, personagens, "pilotos_ids", "pilotos")
    cruzar_dados(veiculos, personagens, "pilotos_ids", "pilotos")

    cruzar_dados(especies, planetas, "planeta_origem_id", "planeta_origem")


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

def inicializar_hashs(planetas, personagens, especies, naves, veiculos):
    hashs = {
        "planetas": {
            "clima": TabelaHash(len(planetas)),
            "terreno": TabelaHash(len(planetas))
        },
        "personagens": {
            "planeta_origem": TabelaHash(len(personagens)),
            "genero": TabelaHash(len(personagens)),
            "nascimento": TabelaHash(len(personagens)),
            "especies": TabelaHash(len(personagens))
        },
        "especies": {
            "classificacao": TabelaHash(len(especies)),
            "planeta_origem": TabelaHash(len(especies)),
            "idioma": TabelaHash(len(especies))
        },
        "naves": {
            "classe_nave": TabelaHash(len(naves)),
            "fabricante": TabelaHash(len(naves))
        },
        "veiculos": {
            "classe_veiculo": TabelaHash(len(veiculos)),
            "modelo": TabelaHash(len(veiculos))
        }
    }

    listas = {
        "planetas": planetas,
        "personagens": personagens,
        "especies": especies,
        "naves": naves,
        "veiculos": veiculos
    }
    
    for i in hashs.items():
        for chave, tabela in i[1].items():
            inserir_hash(listas[i[0]], chave, tabela)
    
    return hashs

def inserir_trie(lista: list, trie: Trie):
    for i in lista:
        trie.inserir(i.nome, i)

def inserir_hash(lista: list, campo, hash: TabelaHash):
    for l in lista:
        atributo = getattr(l, campo)
        tratado = tratar_atributo(atributo)

        for t in tratado:
            hash.inserir(t, l)

def tratar_atributo(atributo):
    if atributo is None:
        return []

    if isinstance(atributo, list):
        chaves = []
        for item in atributo:
            chaves.extend(tratar_atributo(item))
        return chaves

    if hasattr(atributo, "nome"):
        return tratar_atributo(atributo.nome)

    chaves = []
    for parte in str(atributo).split(","):
        parte = parte.strip().lower()
        if parte:
            chaves.append(parte)
    return chaves


def main():
    planetas, personagens, especies, naves, veiculos = carregar_entidades_api()
    
    estabelecer_relacionamentos(planetas, personagens, especies, naves, veiculos)
    
    tries = inicializar_tries(planetas, personagens, especies, naves, veiculos)

    hashs = inicializar_hashs(planetas, personagens, especies, naves, veiculos)

    conjuntos = {
        "planetas": {"trie": tries["planetas"], "hashs": hashs["planetas"]},
        "personagens": {"trie": tries["personagens"], "hashs": hashs["personagens"]},
        "especies": {"trie": tries["especies"], "hashs": hashs["especies"]},
        "naves": {"trie": tries["naves"], "hashs": hashs["naves"]},
        "veiculos": {"trie": tries["veiculos"], "hashs": hashs["veiculos"]}
    }

    exibir_menu_principal(conjuntos)   


if __name__ == "__main__":
    main()