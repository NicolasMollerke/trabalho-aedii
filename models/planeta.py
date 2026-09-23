class Planeta:
    def __init__(self, nome: str, periodo_rotacao: int, periodo_orbita: int, diametro: int, clima: str, gravidade: str, terreno: str, agua: int, populacao: int):
        self.nome = nome
        self.periodo_rotacao = periodo_rotacao
        self.periodo_orbita = periodo_orbita
        self.diametro = diametro
        self.clima = clima
        self.gravidade = gravidade
        self.terreno = terreno
        self.agua = agua
        self.populacao = populacao

    @classmethod
    def criar(cls, dados: dict):
        nome = dados.get("name")
        periodo_rotacao = dados.get("rotation_period")
        periodo_orbita = dados.get("orbital_period")
        diametro = dados.get("diameter")
        clima = dados.get("climate")
        gravidade = dados.get("gravity")
        terreno = dados.get("terrain")
        agua = dados.get("surface_water")
        populacao = dados.get("population")

        return cls(
            nome = nome,
            periodo_rotacao = periodo_rotacao,
            periodo_orbita = periodo_orbita,
            diametro = diametro,
            clima = clima,
            gravidade = gravidade,
            terreno = terreno,
            agua = agua,
            populacao = populacao
        )

    def __repr__(self):
        return f"Planeta('{self.nome}')"
