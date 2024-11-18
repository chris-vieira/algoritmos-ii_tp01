import sys
sys.path.append('./source')

from trie.trieCompacta import TrieCompacta

def printTrie():
    print("--- Trie Compacta ---")
    print("Raiz")
    print(str(trie.raiz.chave) + ": " + str(trie.raiz.valor))
    for i in range(0, trie.raiz.filhos.__len__()):
        print("Filho " + str(i) )
        print(str(trie.raiz.filhos[i].chave) + ": " + str(trie.raiz.filhos[i].valor))
        if trie.raiz.filhos[i].filhos.__len__() > 0:
            for j in range(0, trie.raiz.filhos[i].filhos.__len__()):
                print("Filho " + str(i) + str(j))
                print(str(trie.raiz.filhos[i].filhos[j].chave) + ": " + str(trie.raiz.filhos[i].filhos[j].valor))
                if trie.raiz.filhos[i].filhos[j].filhos.__len__() > 0:
                    for k in range(0, trie.raiz.filhos[i].filhos[j].filhos.__len__()):
                        print("Filho " + str(i) + str(j) +  str(k))
                        print(str(trie.raiz.filhos[i].filhos[j].filhos[k].chave) + ": " + str(trie.raiz.filhos[i].filhos[j].filhos[k].valor))
                        if trie.raiz.filhos[i].filhos[j].filhos[k].filhos.__len__() > 0:
                            for l in range(0, trie.raiz.filhos[i].filhos[j].filhos[k].filhos.__len__()):
                                print("Filho " + str(i) + str(j) +  str(k) +  str(l))
                                print(str(trie.raiz.filhos[i].filhos[j].filhos[k].filhos[l].chave) + ": " + str(trie.raiz.filhos[i].filhos[j].filhos[k].filhos[l].valor))

trie = TrieCompacta()
trie.inserir('by', 21)
trie.inserir('she', 0)
trie.inserir('sea', 10)
trie.inserir('sells', 4)
trie.inserir('shells', 14)
trie.inserir('the', 24)
trie.inserir('sea', 28)


printTrie()


# Teste de Pesquisa do caminho
print()
print("--- Pesquisando o caminho ---")
a = "she"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "sea"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "coelho"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "he"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "mad"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "sells"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "bola"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "b"
print(a + ": " + str(trie.pesquisaCaminho(a)))
a = "sel"
print(a + ": " + str(trie.pesquisaCaminho(a)))

# Teste de Pesquisa 
print()
print("--- Pesquisando ---")
a = "she"
print(a + ": " + str(trie.pesquisar(a)))
a = "sea"
print(a + ": " + str(trie.pesquisar(a)))
a = "coelho"
print(a + ": " + str(trie.pesquisar(a)))
a = "he"
print(a + ": " + str(trie.pesquisar(a)))
a = "mar"
print(a + ": " + str(trie.pesquisar(a)))
a = "sells"
print(a + ": " + str(trie.pesquisar(a)))
a = "bola"
print(a + ": " + str(trie.pesquisar(a)))
a = "b"
print(a + ": " + str(trie.pesquisar(a)))
a = "sel"
print(a + ": " + str(trie.pesquisar(a)))

# Teste de Inserção 
print()
print("--- Inserção ---")
a = "she"
b = 55
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "sea"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "coelho"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "he"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "mar"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "sells"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "bola"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "b"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))
a = "sel"
trie.inserir(a, b)
print(a + ", " + str(b) + ": " + str(trie.pesquisar(a)))


# Teste de remoção
print()
print("--- Remoção ---")
a = "she"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "sea"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "coelho"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "he"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "mar"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "sells"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "bola"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "b"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))
a = "sel"
trie.remover(a)
print(a + ": " + str(trie.pesquisar(a)))

print()
printTrie()
