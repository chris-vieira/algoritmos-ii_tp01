class No:

    def __init__(self, chave: str = '-1', valor = -1):
        self.chave = str(chave)
        self.valor = valor
        self.filhos = []

class TrieCompacta:
    def __init__(self) -> None:
        self.raiz = No()

    def pesquisar(self, chave: str):
        pass        

    def inserir(self, chave, valor):
        pass

    def remover(self, chave, raiz):
        pass