class TabelaHash:
    def __init__(self, x: int):
        self.tam  = x
        self.listas = [[] for i in range(x)]

    def funcao_hash(self, chave):
        return hash(chave) % self.tam

    def inserir(self, chave, objeto):
        indice = self.funcao_hash(chave)
        balde = self.listas[indice]

        for chave_guardada, objetos in balde:
            if chave_guardada == chave:
                objetos.append(objeto)
                return

        balde.append([chave, [objeto]])

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        balde = self.listas[indice]
        
        for chave_guardada, objetos in balde:
            if chave_guardada == chave:
                return objetos

        return None

    def listar_itens(self):
        itens = []
        
        for l in self.listas:
            for chave, objetos in l:
                itens.append((chave, objetos))
        return itens
        
    # def __str__(self) -> str:
    #     linhas = []
    #     for i, balde in enumerate(self.listas):
    #         if not balde:
    #             linhas.append(f"[{i}]: (vazio)")
    #         else:
    #             itens = " -> ".join(f"{chave}: {objeto}" for chave, objeto in balde)
    #             linhas.append(f"[{i}]: {itens}")
    #     return "\n".join(linhas) 

