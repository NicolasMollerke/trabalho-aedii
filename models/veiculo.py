class Veiculo:
    def __init__(
        self,
        id_veiculo: int,
        nome: str,
        modelo: str,
        fabricante: str,
        custo_em_creditos: str,
        comprimento: str,
        velocidade_maxima: str,
        tripulacao: str,
        passageiros: str,
        capacidade_carga: str,
        consumiveis: str,
        classe_veiculo: str,
        pilotos_ids: list,
    ):
        self.id = id_veiculo
        self.nome = nome
        self.modelo = modelo
        self.fabricante = fabricante
        self.custo_em_creditos = custo_em_creditos
        self.comprimento = comprimento
        self.velocidade_maxima= velocidade_maxima
        self.tripulacao = tripulacao
        self.passageiros = passageiros
        self.capacidade_carga = capacidade_carga
        self.consumiveis = consumiveis
        self.classe_veiculo = classe_veiculo

        self.pilotos_ids = pilotos_ids

        self.pilotos = []

    @classmethod
    def criar(cls, dados: dict):
        url = dados.get("url", "")
        id_veiculo = int(url.strip("/").split("/")[-1]) if url else None

        nome = dados.get("name")
        modelo = dados.get("model")
        fabricante = dados.get("manufacturer")
        custo_em_creditos = dados.get("cost_in_credits")
        comprimento = dados.get("length")
        velocidade_maxima = dados.get("max_atmosphering_speed")
        tripulacao = dados.get("crew")
        passageiros = dados.get("passengers")
        capacidade_carga = dados.get("cargo_capacity")
        consumiveis = dados.get("consumables")
        classe_veiculo = dados.get("vehicle_class")

        urls_pilotos = dados.get("pilots", [])
        pilotos_ids = [int(u.strip("/").split("/")[-1]) for u in urls_pilotos if u]

        return cls(
            id_veiculo,
            nome,
            modelo,
            fabricante,
            custo_em_creditos,
            comprimento,
            velocidade_maxima,
            tripulacao,
            passageiros,
            capacidade_carga,
            consumiveis,
            classe_veiculo,
            pilotos_ids,
        )

    def __repr__(self):
        return f"Veiculo('{self.nome}')"

    def exibir_detalhes(self):
            print(f"\nVEÍCULO: {self.nome.upper()}")
            print(f"  • Modelo: {self.modelo}")
            print(f"  • Classe: {self.classe_veiculo.capitalize()}")
            print(f"  • Fabricante: {self.fabricante}")
            print(f"  • Velocidade Máxima: {self.velocidade_maxima}")
            print(f"  • Tripulação / Passageiros: {self.tripulacao} / {self.passageiros}")
            print(f"  • Capacidade de Carga: {self.capacidade_carga}")
            print(f"  • Custo (Créditos): {self.custo_em_creditos}")
            print(f"  • Comprimento: {self.comprimento}m")
            print(f"  • Consumíveis: {self.consumiveis}")
            
            if hasattr(self, 'pilotos') and self.pilotos:
                # Como o __repr__ do Personagem devolve apenas o nome, a lista sairá limpa.
                print(f"  • Pilotos conhecidos: {self.pilotos}")
            else:
                print("  • Pilotos conhecidos: Nenhum registado.")
            print("-" * 40)