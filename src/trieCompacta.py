class No:
    def __init__(self, chave = -1, valor = -1):
        self.chave = str(chave)
        self.valor = valor
        self.filhos = []

class TrieCompacta:
    def __init__(self) -> None:
        self.raiz = No()

    def maiorPrefixo(self, a: str, b: str) -> int:
        r = -1
        # Tamanho da menor palavra recebida
        rep = min(a.__len__(), b.__len__())
        for i in range(0, rep):
            if a[i] != b[i]:
                break
            r = i
        return r+1

    # Retorna um valor i que indica quantas letras da chave foram processadas e uma lista com os indices dos nós partindo da raiz até o nó que possui o valor da chave pesquisada ou deveria possuir o valor da chave (ou seja, a chave pesquisada é menor ou igual a chave do nó) ou o nó pai mais proximo ao nó filho que deveria possuir o valor da chave
    def pesquisaCaminho(self, chave: str) -> tuple[list[int], int]:
        noPai = self.raiz
        # letra atual da chave pesquisada
        i = ri = 0
        r = []
        while noPai.filhos.__len__() > 0 and i < chave.__len__():
            for f in range(0, noPai.filhos.__len__()):
                noAtual = noPai.filhos[f]
                # maiorPrefixoComum é menor ou igual a menor chave passada 
                maiorPrefixoComum = self.maiorPrefixo(str(noAtual.chave), str(chave)[i:])

                if maiorPrefixoComum == 0:
                    if f+1 == noPai.filhos.__len__():
                        return (r, ri)
                    continue

                r.append(f)
                ri += maiorPrefixoComum
                if  chave.__len__() - i < noAtual.chave.__len__():
                    if maiorPrefixoComum > 0:
                        return (r, ri)
                    continue
                elif noAtual.chave.__len__() <  chave.__len__() - i:
                    if noAtual.chave.__len__() == maiorPrefixoComum:
                        noPai = noAtual
                        i += maiorPrefixoComum
                        break
                    else:
                        # Chave do nó já foi toda processada
                        # Mas não bateu completamente com a chave
                        return (r, ri)
                else:
                    if chave.__len__() - i == maiorPrefixoComum:
                        if noAtual.valor != -1:
                            return (r, ri)
                        else:
                            # Chave já foi toda processada
                            # Verifica se exite nó filho sem chave
                            if (noAtual.filhos.__len__() > 0) and noAtual.filhos[0].chave == '':
                                r.append(0)
                                # Apenas nós folha possuem valor
                                return (r, ri)
                            else:
                                # Não possui valor no nó encontrado
                                return (r, ri)
                    else:
                        # Chave já foi toda processada
                        # Mas a chave não bateu com o nó atual
                        return (r, ri)             
        return (r, ri)

    def pesquisar(self, chave: str):
        caminho, letrasProcesadas = self.pesquisaCaminho(chave)
    
        if letrasProcesadas < chave.__len__():
            return -1
        
        noAtual = self.raiz
        for i in range(0, caminho.__len__()):
            noAtual = noAtual.filhos[caminho[i]]

        if self.maiorPrefixo(chave[::-1], noAtual.chave[::-1]) != noAtual.chave.__len__():
            return -1
        
        return noAtual.valor


    def inserir(self, chave, valor):

        pass

    def remover(self, chave, raiz):
        pass
    