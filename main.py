import requests
from models.planeta import Planeta
from models.personagem import Personagem
from models.especie import Especie
from models.nave import Nave
from models.veiculo import Veiculo
from estruturas.trie import Trie
from estruturas.hash import TabelaHash
from estruturas.arvoreb import ArvoreB
from menus.principal import exibir_menu_principal
from servicos.galaxia import montar_grafo


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
            "clima": TabelaHash(),
            "terreno": TabelaHash()
        },
        "personagens": {
            "planeta_origem": TabelaHash(),
            "genero": TabelaHash(),
            "nascimento": TabelaHash(),
            "especies": TabelaHash()
        },
        "especies": {
            "classificacao": TabelaHash(),
            "planeta_origem": TabelaHash(),
            "idioma": TabelaHash()
        },
        "naves": {
            "classe_nave": TabelaHash(),
            "fabricante": TabelaHash()
        },
        "veiculos": {
            "classe_veiculo": TabelaHash(),
            "modelo": TabelaHash()
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

def inicializar_arvores(planetas, personagens, especies, naves, veiculos):
    arvores = {
        "planetas": {
            "diametro": ArvoreB(),
            "populacao":  ArvoreB()
        },
        "personagens": {
            "altura":  ArvoreB(),
            "peso":  ArvoreB()
        },
        "especies": {
            "altura_media": ArvoreB(),
            "expectativa_vida": ArvoreB()
        },
        "naves": {
            "custo_em_creditos": ArvoreB(),
            "classe_hiperdrive": ArvoreB(),
            "capacidade_carga": ArvoreB(),
            "passageiros": ArvoreB(),
        },
        "veiculos": {
            "velocidade_maxima": ArvoreB(),
            "passageiros": ArvoreB(),
            "custo_em_creditos": ArvoreB(),

        }
    }

    listas = {
        "planetas": planetas,
        "personagens": personagens,
        "especies": especies,
        "naves": naves,
        "veiculos": veiculos
    }
    
    for i in arvores.items():
        for chave, arvore in i[1].items():
            inserir_arvore(listas[i[0]], chave, arvore)
    
    return arvores

def inserir_trie(lista: list, trie: Trie):
    for i in lista:
        trie.inserir(i.nome, i)

def inserir_hash(lista: list, campo, hash: TabelaHash):
    for l in lista:
        atributo = getattr(l, campo)
        tratado = tratar_atributo(atributo)

        for t in tratado:
            hash.inserir(t, l)

def inserir_arvore(lista: list, campo, arvore: ArvoreB):
    for l in lista:
        atributo = getattr(l, campo)
        tratado = converter_numero(atributo)

        if tratado is not None:
            arvore.inserir(tratado, l)

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

def converter_numero(valor):
    if valor is None:
        return None

    texto = str(valor).strip().lower()

    if texto in ("", "unknown", "n/a", "none"):
        return None

    texto = texto.replace(",", "")

    try:
        return float(texto)
    except ValueError:
        return None


def main():
    planetas, personagens, especies, naves, veiculos = carregar_entidades_api()

    grafo_planetas = montar_grafo(planetas)
    print(len(grafo_planetas.vertices))
    
    estabelecer_relacionamentos(planetas, personagens, especies, naves, veiculos)
    
    tries = inicializar_tries(planetas, personagens, especies, naves, veiculos)

    hashs = inicializar_hashs(planetas, personagens, especies, naves, veiculos)

    arvores = inicializar_arvores(planetas, personagens, especies, naves, veiculos)

    conjuntos = {
        "planetas": {"trie": tries["planetas"], "hashs": hashs["planetas"], "arvores": arvores["planetas"], "grafo": grafo_planetas},
        "personagens": {"trie": tries["personagens"], "hashs": hashs["personagens"], "arvores": arvores["personagens"]},
        "especies": {"trie": tries["especies"], "hashs": hashs["especies"], "arvores": arvores["especies"]},
        "naves": {"trie": tries["naves"], "hashs": hashs["naves"], "arvores": arvores["naves"]},
        "veiculos": {"trie": tries["veiculos"], "hashs": hashs["veiculos"], "arvores": arvores["veiculos"]}
    }

    exibir_menu_principal(conjuntos)   


if __name__ == "__main__":
    main()