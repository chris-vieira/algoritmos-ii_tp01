class No:
    def __init__(self, chave = -1, valor = -1):
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
                # maiorPrefixoComum é menor ou igual a menor chave passada 
                maiorPrefixoComum = self.maiorPrefixo(str(noAtual.chave), str(chave)[i:])

                if maiorPrefixoComum == 0:
                    if f+1 == noPai.filhos.__len__():
                        return -1
                    continue

                if  chave.__len__() - i < noAtual.chave.__len__() :
                    if maiorPrefixoComum > 0:
                        return -1
                    continue
                elif noAtual.chave.__len__() <  chave.__len__() - i:
                    if noAtual.chave.__len__() == maiorPrefixoComum:
                        noPai = noAtual
                        i += maiorPrefixoComum
                        break
                    else:
                        # Chave do nó já foi toda processada
                        # Mas não bateu completamente com a chave
                        return -1
                else:
                    if chave.__len__() - i == maiorPrefixoComum:
                        if noAtual.valor != -1:
                            return noAtual.valor
                        else:
                            # Chave já foi toda processada
                            # Verifica se exite nó filho sem chave
                            if (noAtual.filhos.__len__() > 0) and noAtual.filhos[0].chave == '':
                                # Apenas nós folha possuem valor
                                return noAtual.filhos[0].valor
                            else:
                                # Não possui valor no nó encontrado
                                return -1
                    else:
                        # Chave já foi toda processada
                        # Mas a chave não bateu com o nó atual
                        return -1           

        print("A pesquisa não trata todos os casos!")     
        return -1

    def inserir(self, chave, valor):
        pass

    def remover(self, chave, raiz):
        pass
    