class Personagem:
    def __init__(
        self,
        id_personagem: int,
        nome: str,
        altura: str,
        peso: str,
        cor_cabelo: str,
        cor_pele: str,
        cor_olho: str,
        nascimento: str,
        planeta_origem_id: int,
        especies_ids: list,
        veiculos_ids: list,
        naves_ids: list
    ):
        self.id = id_personagem
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.cor_cabelo = cor_cabelo
        self.cor_pele = cor_pele
        self.cor_olho = cor_olho
        self.nascimento = nascimento
        self.planeta_origem_id = planeta_origem_id
        self.especies_ids = especies_ids
        self.veiculos_ids = veiculos_ids
        self.naves_ids = naves_ids

        self.planeta_origem = None
        self.especies = []
        self.veiculos = []
        self.naves = []

    @classmethod
    def criar(cls, dados: dict):
        url = dados.get("url")

        id = int(url.strip("/").split("/")[-1])
        nome = dados.get("name")
        altura = dados.get("height")
        peso = dados.get("mass")
        cor_cabelo = dados.get("hair_color")
        cor_pele = dados.get("skin_color")
        cor_olho = dados.get("eye_color")
        nascimento = dados.get("birth_year")

        url_planeta_origem = dados.get("homeworld", "")
        planeta_origem_id = int(url_planeta_origem.strip("/").split("/")[-1]) if url_planeta_origem else None

        urls_especies = dados.get("species")
        especies_ids = [int(u.strip("/").split("/")[-1]) for u in urls_especies if u]

        urls_veiculos = dados.get("vehicles")
        veiculos_ids = [int(u.strip("/").split("/")[-1]) for u in urls_veiculos if u]

        urls_naves = dados.get("starships")
        naves_ids = [int(u.strip("/").split("/")[-1]) for u in urls_naves if u]

        return cls(
            id,
            nome,
            altura,
            peso,
            cor_cabelo,
            cor_pele,
            cor_olho,
            nascimento,
            planeta_origem_id,
            especies_ids,
            veiculos_ids,
            naves_ids
        )

    def __repr__(self):
        return f"Personagem('{self.nome}')"

    def exibir_detalhes(self):
        print(f"\nPERSONAGEM: {self.nome.upper()}")
        print(f"  • Ano de Nascimento: {self.nascimento}")
        print(f"  • Altura / Peso: {self.altura} cm / {self.peso} kg")
        print(f"  • Cor do Cabelo: {self.cor_cabelo}")
        print(f"  • Cor dos Olhos: {self.cor_olho}")
        print(f"  • Cor da Pele: {self.cor_pele}")
        
        if hasattr(self, 'planeta_origem') and self.planeta_origem:
            print(f"  • Planeta de Origem: {self.planeta_origem}")
        else:
            print("  • Planeta de Origem: Desconhecido")
        
        if hasattr(self, 'especies') and self.especies:
            print(f"  • Espécie(s): {self.especies}")
        else:
            print("  • Espécie(s): Desconhecida / Humano")

        if hasattr(self, 'veiculos') and self.veiculos:
            print(f"  • Veículo(s): {self.veiculos}")
        
        if hasattr(self, 'naves') and self.naves:
            print(f"  • Nave(s): {self.naves}")
            
        print("-" * 40)