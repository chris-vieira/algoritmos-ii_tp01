class No:
    def __init__(self, chave = None, valor = None):
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

    # Retorna um valor i que indica quantas letras da chave foram processadas nos nós pai ao ultimo da lista e uma lista com os indices dos nós partindo da raiz até o nó que possui o valor da chave pesquisada ou deveria possuir o valor da chave (ou seja, a chave pesquisada é menor ou igual a chave do nó) ou o nó pai mais proximo ao nó filho que deveria possuir o valor da chave
    def pesquisaCaminho(self, chave) -> tuple[list[int], int]:
        noPai = self.raiz
        # letra atual da chave pesquisada
        i = 0
        r = []
        while noPai.filhos.__len__() > 0 and i < str(chave).__len__():
            for f in range(0, noPai.filhos.__len__()):
                noAtual = noPai.filhos[f]
                # maiorPrefixoComum é menor ou igual a menor chave passada 
                maiorPrefixoComum = self.maiorPrefixo(str(noAtual.chave), str(chave)[i:])

                if maiorPrefixoComum <= 0:
                    if f+1 == noPai.filhos.__len__():
                        return (r, i)
                    continue

                r.append(f)
                if  str(chave)[i:].__len__() < noAtual.chave.__len__():
                    if maiorPrefixoComum > 0:
                        return (r, i)
                    continue
                elif noAtual.chave.__len__() <  str(chave)[i:].__len__():
                    if noAtual.chave.__len__() == maiorPrefixoComum:
                        i += maiorPrefixoComum
                        noPai = noAtual
                        break
                    else:
                        # Chave do nó já foi toda processada
                        # Mas não bateu completamente com a chave
                        return (r, i)
                else:
                    if str(chave)[i:].__len__() == maiorPrefixoComum:
                        i += maiorPrefixoComum
                        # O valor pode estar no nó atual ou nos N primeiros filhos sendo N é o número de vezes que a chave pesquisada foi inserida
                        return (r,  i)
                    else:
                        # Chave já foi toda processada
                        # Mas a chave não bateu com o nó atual
                        return (r, i)             
        return (r, i)

    def pesquisar(self, chave):
        caminho, letrasProcesadas = self.pesquisaCaminho(chave)
    
        if letrasProcesadas < str(chave).__len__():
            return None
        
        noAtual = self.raiz
        for i in range(0, caminho.__len__()):
            noAtual = noAtual.filhos[caminho[i]]

        if self.maiorPrefixo(str(chave)[::-1], str(noAtual.chave)[::-1]) != noAtual.chave.__len__():
            return None
        
        # No caso do nó não possuir o valor, os N primeiro filhos devem possuir
        if noAtual.valor == None and noAtual.filhos.__len__() > 0:
            r = []

            for i in range(0, noAtual.filhos.__len__()):
                if noAtual.filhos[i].chave == '':
                    r.append(noAtual.filhos[i].valor)
                else:
                    break

            if r.__len__() == 1:
                return r[0]

            return r
        
        return noAtual.valor

    def inserir(self, chave, valor):
        caminho, letrasProcesadas = self.pesquisaCaminho(chave)

        noAtual = self.raiz
        if letrasProcesadas == 0 and caminho == []:
            noAtual.filhos.append(No(chave, valor))
            return

        for i in range(0, caminho.__len__()):
            noAtual = noAtual.filhos[caminho[i]]

        maiorPrefixoComum = self.maiorPrefixo(str(noAtual.chave), str(chave)[letrasProcesadas:])

        if maiorPrefixoComum == 0:
            if noAtual.filhos.__len__() == 0:
                noAtual.filhos.insert(0, No('', noAtual.valor))
                noAtual.valor = None
            
            if str(chave)[maiorPrefixoComum+letrasProcesadas:] == '':
                noAtual.filhos.insert(0, No(str(chave)[maiorPrefixoComum+letrasProcesadas:], valor))
            else:
                noAtual.filhos.append(No(str(chave)[maiorPrefixoComum+letrasProcesadas:], valor))
            return

        if maiorPrefixoComum > 0:
            if str(noAtual.chave).__len__() > maiorPrefixoComum:
                filhosAux = noAtual.filhos
                noAtual.filhos = []
                noAtual.filhos.append(No(noAtual.chave[maiorPrefixoComum:], noAtual.valor))
                noAtual.filhos[0].filhos = filhosAux
                noAtual.chave = noAtual.chave[:maiorPrefixoComum]
                noAtual.valor = None

                if str(chave)[maiorPrefixoComum+letrasProcesadas:] == '':
                    noAtual.filhos.insert(0, No(str(chave)[maiorPrefixoComum+letrasProcesadas:], valor))
                else:
                    noAtual.filhos.append(No(str(chave)[maiorPrefixoComum+letrasProcesadas:], valor))
                return
        return -1

    def remover(self, chave):
        caminho, letrasProcesadas = self.pesquisaCaminho(chave)

        noAtual = self.raiz
        if letrasProcesadas != str(chave).__len__() :
            return -1

        nos = [noAtual]
        for i in range(0, caminho.__len__()):
            noAtual = noAtual.filhos[caminho[i]]
            nos.append(noAtual)

        tamNos = nos.__len__()
        if nos[tamNos-1].filhos.__len__() > 0:
            for j in range(0, nos[tamNos-1].filhos.__len__()):
                if nos[tamNos-1].filhos[0].chave == '':
                    nos[tamNos-1].filhos.pop(0)
                else:
                    break

        if nos[tamNos-1].filhos.__len__() == 0:
            nos[tamNos-2].filhos.pop(caminho[caminho.__len__()-1])

        # Verifica o nó pai(ou o folha com o valor) tem apenas um filho e os une
        if nos[tamNos-1].filhos.__len__() == 1:
            nos[tamNos-1].chave = str(nos[tamNos-1].chave) + str(nos[tamNos-1].filhos[0].chave)
            nos[tamNos-1].valor = nos[tamNos-1].filhos[0].valor
            filhosAux = nos[tamNos-1].filhos[0].filhos
            nos[tamNos-1].filhos.pop(0)
            nos[tamNos-1].filhos = filhosAux

        # Verifica o nó vo(ou o pai) tem apenas um filho e os une
        if nos[tamNos-2].filhos.__len__() == 1:
            nos[tamNos-2].chave = str(nos[tamNos-2].chave) + str(nos[tamNos-2].filhos[0].chave)
            nos[tamNos-2].valor = nos[tamNos-2].filhos[0].valor
            filhosAux = nos[tamNos-2].filhos[0].filhos
            nos[tamNos-2].filhos.pop(0)
            nos[tamNos-2].filhos = filhosAux
        return
