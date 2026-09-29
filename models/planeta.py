class Planeta:
    def __init__(
        self,
        id: int, 
        nome: str, 
        periodo_rotacao: int, 
        periodo_orbita: int, 
        diametro: int, clima: str, 
        gravidade: str, 
        terreno: str, 
        agua: int, 
        populacao: int,
        residentes_ids: list
    ):
        self.id = id
        self.nome = nome
        self.periodo_rotacao = periodo_rotacao
        self.periodo_orbita = periodo_orbita
        self.diametro = diametro
        self.clima = clima
        self.gravidade = gravidade
        self.terreno = terreno
        self.agua = agua
        self.populacao = populacao
        self.residentes_ids = residentes_ids

        self.residentes = []

    @classmethod
    def criar(cls, dados: dict):
        url = dados.get("url")

        id = int(url.strip("/").split("/")[-1])
        nome = dados.get("name")
        periodo_rotacao = dados.get("rotation_period")
        periodo_orbita = dados.get("orbital_period")
        diametro = dados.get("diameter")
        clima = dados.get("climate")
        gravidade = dados.get("gravity")
        terreno = dados.get("terrain")
        agua = dados.get("surface_water")
        populacao = dados.get("population")

        urls_residentes = dados.get("residents")
        residentes_ids = [int(u.strip("/").split("/")[-1]) for u in urls_residentes if u]

        return cls(
            id,
            nome,
            periodo_rotacao,
            periodo_orbita,
            diametro,
            clima,
            gravidade,
            terreno,
            agua,
            populacao,
            residentes_ids
        )

    def __repr__(self):
        return f"{self.nome}"

    def exibir_detalhes(self):
        print(f"\nPLANETA: {self.nome.upper()}")
        print(f"  • Clima: {self.clima}")
        print(f"  • Terreno: {self.terreno}")
        print(f"  • População: {self.populacao}")
        print(f"  • Gravidade: {self.gravidade}")
        print(f"  • Diâmetro: {self.diametro}")
        print(f"  • Período de Rotação: {self.periodo_rotacao} horas")
        print(f"  • Período de Órbita: {self.periodo_orbita} dias")
        print(f"  • Água na Superfície: {self.agua}%")
        
        if hasattr(self, 'residentes') and self.residentes:
            print(f"  • Residentes conhecidos: {self.residentes}")
        else:
            print("  • Residentes conhecidos: Nenhum registado.")
        print("-" * 40)

