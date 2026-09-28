class NoTrie:
    def __init__(self):
        self.filhos = [None] * 256
        self.fim_de_palavra = False
        self.dados = None 

class Trie:
    def __init__(self):
        self.raiz = NoTrie()
        self.nos_visitados = 0 

    def _obter_indice(self, char):
        return ord(char)

    def inserir(self, chave, dados):
        chave = chave.lower()
        
        no_atual = self.raiz
        for char in chave:
            indice = self._obter_indice(char)
            if not no_atual.filhos[indice]:
                no_atual.filhos[indice] = NoTrie()
            no_atual = no_atual.filhos[indice]
        no_atual.fim_de_palavra = True
        no_atual.dados = dados

    def buscar(self, chave):
        self.nos_visitados = 0
        no_atual = self.raiz

        chave = chave.lower()
        
        for char in chave:
            self.nos_visitados += 1
            indice = self._obter_indice(char)
            
            if not no_atual.filhos[indice]:
                print("Não encontrado")
                return None
            no_atual = no_atual.filhos[indice]
            
        if no_atual is not None and no_atual.fim_de_palavra:
            return no_atual.dados, self.nos_visitados
        return None

    def buscaPrefixo(self, prefixo: str) -> list:
        resultados = []
        no = self.raiz
        self.nos_visitados = 0

        prefixo = prefixo.lower()

        for char in prefixo:
            self.nos_visitados += 1
            indice = self._obter_indice(char)

            if no.filhos[indice] is None:
                return resultados, self.nos_visitados

            no = no.filhos[indice]

        self.buscaRecursiva(prefixo, no, resultados)

        return resultados, self.nos_visitados


    def buscaRecursiva(self, prefixo, no, resultados):
        if no.fim_de_palavra:
            resultados.append(no.dados)

        for indice, proxNo in enumerate(no.filhos):
            if proxNo is not None:
                self.nos_visitados += 1
                letra = chr(indice)
                self.buscaRecursiva(prefixo + letra, proxNo, resultados)

