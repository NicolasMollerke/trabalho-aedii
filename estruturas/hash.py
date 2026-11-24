class TabelaHash:
    def __init__(self):
        self.tam  = 8
        self.listas = [[] for i in range(self.tam)]
        self.colisoes = 0
        self.chaves = 0

    def funcao_hash(self, chave):
        texto = str(chave)
        acumulador = 0
        for caractere in texto:
            acumulador = (acumulador * 31 + ord(caractere)) % self.tam
        return acumulador
    
    def inserir(self, chave, objeto):
        indice = self.funcao_hash(chave)
        balde = self.listas[indice]

        for chave_guardada, objetos in balde:
            if chave_guardada == chave:
                objetos.append(objeto)
                return

        if balde:
            self.colisoes += 1

        balde.append([chave, [objeto]])
        self.chaves += 1

        if self.chaves / self.tam > 0.75:
            self.redimensionar()

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

    def redimensionar(self):
        temp = self.listas

        self.tam = self.tam * 2

        self.listas = [[] for i in range(self.tam)]

        for balde in temp:
            for par in balde:
                chave = par[0]
                indice = self.funcao_hash(chave)
                self.listas[indice].append(par)

    def fator_carga(self):
        return self.chaves / self.tam


        
    # def __str__(self) -> str:
    #     linhas = []
    #     for i, balde in enumerate(self.listas):
    #         if not balde:
    #             linhas.append(f"[{i}]: (vazio)")
    #         else:
    #             itens = " -> ".join(f"{chave}: {objeto}" for chave, objeto in balde)
    #             linhas.append(f"[{i}]: {itens}")
    #     return "\n".join(linhas) 

