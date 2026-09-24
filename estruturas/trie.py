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
            return no_atual.dados
        return None
