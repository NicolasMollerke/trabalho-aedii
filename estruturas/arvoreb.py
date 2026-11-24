class NoArvoreB:
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []    
        self.valores = []  
        self.filhos = []   

class ArvoreB:
    def __init__(self, t=3):
        if t < 2:
            raise ValueError("O grau mínimo t deve ser pelo menos 2.")
        self.t = t
        self.raiz = NoArvoreB(folha=True)
        self.nos_visitados = 0
        self.splits = 0

    def buscar(self, chave):
        self.nos_visitados = 0
        encontrado = self._buscar_no(self.raiz, chave)
        if encontrado is None:
            return []
        no, i = encontrado
        return list(no.valores[i])

    def _buscar_no(self, no, chave):
        self.nos_visitados += 1
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1

        if i < len(no.chaves) and chave == no.chaves[i]:
            return no, i
        if no.folha:
            return None
        return self._buscar_no(no.filhos[i], chave)

    def inserir(self, chave, objeto):
        encontrado = self._buscar_no(self.raiz, chave)
        if encontrado is not None:
            no, i = encontrado
            no.valores[i].append(objeto)
            return

        raiz = self.raiz
        if len(raiz.chaves) == 2 * self.t - 1:
            nova_raiz = NoArvoreB(folha=False)
            nova_raiz.filhos.append(raiz)
            self.raiz = nova_raiz
            self.dividir_filho(nova_raiz, 0)
            self.inserir_nao_cheio(nova_raiz, chave, objeto)
        else:
            self.inserir_nao_cheio(raiz, chave, objeto)

    def inserir_nao_cheio(self, no, chave, objeto):
        i = len(no.chaves) - 1

        if no.folha:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            no.chaves.insert(i + 1, chave)
            no.valores.insert(i + 1, [objeto])
        else:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1

            if len(no.filhos[i].chaves) == 2 * self.t - 1:
                self.dividir_filho(no, i)
                if chave > no.chaves[i]:
                    i += 1

            self.inserir_nao_cheio(no.filhos[i], chave, objeto)

    def dividir_filho(self, pai, i):
        t = self.t
        cheio = pai.filhos[i]                 
        novo = NoArvoreB(folha=cheio.folha)
        self.splits += 1

        chave_meio = cheio.chaves[t - 1]
        valor_meio = cheio.valores[t - 1]

        novo.chaves = cheio.chaves[t:]
        novo.valores = cheio.valores[t:]
        if not cheio.folha:
            novo.filhos = cheio.filhos[t:]   
            cheio.filhos = cheio.filhos[:t]   

        cheio.chaves = cheio.chaves[:t - 1]
        cheio.valores = cheio.valores[:t - 1]


        pai.chaves.insert(i, chave_meio)
        pai.valores.insert(i, valor_meio)
        pai.filhos.insert(i + 1, novo)

    def buscar_intervalo(self, minimo, maximo):
        self.nos_visitados = 0
        resultados = []
        self.intervalo(self.raiz, minimo, maximo, resultados)
        
        return resultados

    def intervalo(self, no, minimo, maximo, resultados):
        self.nos_visitados += 1

        for i in range(len(no.chaves)):
            chave = no.chaves[i]

            if not no.folha and (minimo is None or minimo < chave):
                self.intervalo(no.filhos[i], minimo, maximo, resultados)

            if maximo is not None and chave > maximo:
                return

            if minimo is None or chave >= minimo:
                resultados.extend(no.valores[i])

        if not no.folha:
            self.intervalo(no.filhos[-1], minimo, maximo, resultados)

    def altura(self):
        no = self.raiz
        altura = 0
        while not no.folha:
            no = no.filhos[0]
            altura += 1
        return altura

    def exibir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        print(f"Nível {nivel}: {no.chaves}")
        for filho in no.filhos:
            self.exibir(filho, nivel + 1)