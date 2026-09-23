import requests
from models.planeta import Planeta


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

def cria_objetos(dados: list, classe: type):
    lista_objetos = []

    for d in dados:
        objeto = classe.criar(d)
        lista_objetos.append(objeto)

    return lista_objetos

    

def main():
    dados = fetch_data("planets")
    lista_planetas = cria_objetos(dados, Planeta)
    print(lista_planetas)

if __name__ == "__main__":
    main()