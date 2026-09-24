class Especie:
    def __init__(
        self,
        id_especie: int,
        nome: str,
        classificacao: str,
        designacao: str,
        altura_media: str,
        cores_pele: str,
        cores_cabelo: str,
        cores_olhos: str,
        expectativa_vida: str,
        planeta_origem_id: int,
        idioma: str,
        personagens_ids: list,
    ):
        self.id = id_especie
        self.nome = nome
        self.classificacao = classificacao
        self.designacao = designacao
        self.altura_media = altura_media
        self.cores_pele = cores_pele
        self.cores_cabelo = cores_cabelo
        self.cores_olhos = cores_olhos
        self.expectativa_vidaa = expectativa_vida
        self.planeta_origem_id = planeta_origem_id
        self.idioma = idioma

        self.personagens_ids = personagens_ids

        self.planeta_origem = None
        self.personagens = []

    @classmethod
    def criar(cls, dados: dict):
        url = dados.get("url", "")
        id_especie = int(url.strip("/").split("/")[-1]) if url else None

        nome = dados.get("name")
        classificacao = dados.get("classification")
        designacao = dados.get("designation")
        altura_media = dados.get("average_height")
        cores_pele = dados.get("skin_colors")
        cores_cabelo = dados.get("hair_colors")
        cores_olhos = dados.get("eye_colors")
        expectativa_vida = dados.get("average_lifespan")

        url_planeta_origem = dados.get("homeworld", "")
        planeta_origem_id = int(url_planeta_origem.strip("/").split("/")[-1]) if url_planeta_origem else None

        idioma = dados.get("language")

        urls_personagens = dados.get("people", [])
        personagens_ids = [int(u.strip("/").split("/")[-1]) for u in urls_personagens if u]

        return cls(
            id_especie,
            nome,
            classificacao,
            designacao,
            altura_media,
            cores_pele,
            cores_cabelo,
            cores_olhos,
            expectativa_vida,
            planeta_origem_id,
            idioma,
            personagens_ids,
        )

    def __repr__(self):
        return f"Especie('{self.nome}')"