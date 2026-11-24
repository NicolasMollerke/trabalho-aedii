def aplicar_filtro(titulo, opcoes, arvores):
    while True:
        print(f"\n=== {titulo} ===")
        for numero, (descricao, _, _, _) in opcoes.items():
            print(f"[{numero}] {descricao}")
        print("[0] Voltar")

        opcao = input("Escolha o filtro: ").strip()

        if opcao == "0":
            return None, None

        if opcao not in opcoes:
            print("Opção inválida!")
            continue

        _, atributo, minimo, maximo = opcoes[opcao]

        arvore = arvores[atributo]
        resultados = arvore.buscar_intervalo(minimo, maximo)
        texto = (
            f"Altura: {arvore.altura()} | "
            f"Splits: {arvore.splits}"
        )

        return resultados, texto


def filtrar_planetas(arvores):
    opcoes = {
        "1": ("Planetas Gigantes (Diâmetro >= 15.000 km)", "diametro", 15000, None),
        "2": ("Planetas Pequenos (Diâmetro <= 10.000 km)", "diametro", None, 10000),
        "3": ("Superpopulosos (População >= 1.000.000.000)", "populacao", 1000000000, None),
    }
    return aplicar_filtro("FILTRAR PLANETAS", opcoes, arvores)


def filtrar_personagens(arvores):
    opcoes = {
        "1": ("Personagens Altos (Altura >= 200 cm)", "altura", 200, None),
        "2": ("Personagens Baixos (Altura <= 150 cm)", "altura", None, 150),
        "3": ("Personagens Pesados (Massa >= 100 kg)", "peso", 100, None),
        "4": ("Personagens Leves (Massa <= 50 kg)", "peso", None, 50),
    }
    return aplicar_filtro("FILTRAR PERSONAGENS", opcoes, arvores)


def filtrar_naves(arvores):
    opcoes = {
        "1": ("Naves Caras (Custo >= 1.000.000 créditos)", "custo_em_creditos", 1000000, None),
        "2": ("Naves Rápidas (Hyperdrive <= 1.0)", "classe_hiperdrive", None, 1.0),
        "3": ("Super Cargueiros (Capacidade >= 50.000 kg)", "capacidade_carga", 50000, None),
        "4": ("Naves de Transporte (Passageiros >= 100)", "passageiros", 100, None),
    }
    return aplicar_filtro("FILTRAR NAVES", opcoes, arvores)


def filtrar_veiculos(arvores):
    opcoes = {
        "1": ("Veículos Muito Rápidos (Velocidade >= 1.000 km/h)", "velocidade_maxima", 1000, None),
        "2": ("Veículos de Transporte (Passageiros >= 30)", "passageiros", 30, None),
        "3": ("Veículos Caros (Custo >= 50.000 créditos)", "custo_em_creditos", 50000, None),
        "4": ("Veículos Individuais (Passageiros = 0)", "passageiros", 0, 0),
    }
    return aplicar_filtro("FILTRAR VEÍCULOS", opcoes, arvores)


def filtrar_especies(arvores):
    opcoes = {
        "1": ("Espécies Longevas (Expectativa de Vida >= 100 anos)", "expectativa_vida", 100, None),
        "2": ("Espécies de Vida Curta (Expectativa de Vida <= 50 anos)", "expectativa_vida", None, 50),
        "3": ("Espécies Altas (Altura Média >= 180 cm)", "altura_media", 180, None),
        "4": ("Espécies Baixas (Altura Média <= 150 cm)", "altura_media", None, 150),
    }
    return aplicar_filtro("FILTRAR ESPÉCIES", opcoes, arvores)