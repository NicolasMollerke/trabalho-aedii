class Nave:
    def __init__(
        self,
        id_nave: int,
        nome: str,
        modelo: str,
        fabricante: str,
        custo_em_creditos: str,
        comprimento: str,
        velocidade_maxima_atmosferica: str,
        tripulacao: str,
        passageiros: str,
        capacidade_carga: str,
        consumiveis: str,
        classe_hiperdrive: str,
        mglt: str,
        classe_nave: str,
        pilotos_ids: list,
    ):
        self.id = id_nave
        self.nome = nome
        self.modelo = modelo
        self.fabricante = fabricante
        self.custo_em_creditos = custo_em_creditos
        self.comprimento = comprimento
        self.velocidade_maxima_atmosferica = velocidade_maxima_atmosferica
        self.tripulacao = tripulacao
        self.passageiros = passageiros
        self.capacidade_carga = capacidade_carga
        self.consumiveis = consumiveis
        self.classe_hiperdrive = classe_hiperdrive
        self.mglt = mglt
        self.classe_nave = classe_nave

        self.pilotos_ids = pilotos_ids

        self.pilotos = []

    @classmethod
    def criar(cls, dados: dict):
        url = dados.get("url", "")
        id_nave = int(url.strip("/").split("/")[-1]) if url else None

        nome = dados.get("name")
        modelo = dados.get("model")
        fabricante = dados.get("manufacturer")
        custo_em_creditos = dados.get("cost_in_credits")
        comprimento = dados.get("length")
        velocidade_maxima_atmosferica = dados.get("max_atmosphering_speed")
        tripulacao = dados.get("crew")
        passageiros = dados.get("passengers")
        capacidade_carga = dados.get("cargo_capacity")
        consumiveis = dados.get("consumables")
        classe_hiperdrive = dados.get("hyperdrive_rating")
        mglt = dados.get("MGLT")
        classe_nave = dados.get("starship_class")

        urls_pilotos = dados.get("pilots", [])
        pilotos_ids = [int(u.strip("/").split("/")[-1]) for u in urls_pilotos if u]

        return cls(
            id_nave,
            nome,
            modelo,
            fabricante,
            custo_em_creditos,
            comprimento,
            velocidade_maxima_atmosferica,
            tripulacao,
            passageiros,
            capacidade_carga,
            consumiveis,
            classe_hiperdrive,
            mglt,
            classe_nave,
            pilotos_ids,

        )

    def __repr__(self):
        return f"Nave('{self.nome}')"

    def exibir_detalhes(self):
        print(f"\n NAVE: {self.nome.upper()}")
        print(f"  • Modelo: {self.modelo}")
        print(f"  • Classe: {self.classe_nave.capitalize()}")
        print(f"  • Fabricante: {self.fabricante}")
        print(f"  • Velocidade Máx. Atmosférica: {self.velocidade_maxima_atmosferica}")
        print(f"  • Classe de Hyperdrive: {self.classe_hiperdrive}")
        print(f"  • MGLT (Megalights): {self.mglt}")
        print(f"  • Tripulação / Passageiros: {self.tripulacao} / {self.passageiros}")
        print(f"  • Capacidade de Carga: {self.capacidade_carga}")
        print(f"  • Custo (Créditos): {self.custo_em_creditos}")
        print(f"  • Comprimento: {self.comprimento}m")
        print(f"  • Consumíveis: {self.consumiveis}")
        
        if hasattr(self, 'pilotos') and self.pilotos:
            print(f"  • Pilotos conhecidos: {self.pilotos}")
        else:
            print("  • Pilotos conhecidos: Nenhum registado.")
        print("-" * 40)