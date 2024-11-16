class No:
    def __init__(self, chave: str = '-1', valor = -1):
        self.chave = str(chave)
        self.valor = valor
        self.filhos = []

class TrieCompacta:
    def __init__(self) -> None:
        self.raiz = No()

    def maiorPrefixo(self, a: str, b: str):
        r = -1
        # Tamanho da menor palavra recebida
        rep = min(a.__len__(), b.__len__())
        for i in range(0, rep):
            if a[i] != b[i]:
                break
            r = i
        return r+1

    def pesquisar(self, chave: str):
        noPai = self.raiz
        # letra atual da chave pesquisada
        i = 0
        while noPai.filhos.__len__() > 0 and i < chave.__len__():
            for f in range(0, noPai.filhos.__len__()):
                noAtual = noPai.filhos[f]
                maiorPrefixoComum = self.maiorPrefixo(noAtual.chave, chave[i:])

                # IMPORTANTE: REVISAR SE TODAS POSSIBILIDADE ESTÂO COBERTAS
                if maiorPrefixoComum == 0:
                    if f+1 == noPai.filhos.__len__():
                        return -1
                    continue

                if chave.__len__() - i < noAtual.chave.__len__() :
                    if maiorPrefixoComum > 0:
                        return -1
                    continue

                if chave.__len__() - i == noAtual.chave.__len__():
                    if noAtual.chave.__len__() == maiorPrefixoComum:
                        if noAtual.valor == -1:
                            # Chave já foi toda processada
                            # Verifica se exite nó filho sem chave
                            if (noAtual.filhos.__len__() > 0) and noAtual.filhos[0].chave == '':
                                return noAtual.filhos[0].valor
                            else:
                                return -1
                        return noAtual.valor
                    else:
                        return -1
                
                if noAtual.chave.__len__() == maiorPrefixoComum:
                    noPai = noAtual
                    i += maiorPrefixoComum
                    break
        return -1

    def inserir(self, chave, valor):
        pass

    def remover(self, chave, raiz):
        pass