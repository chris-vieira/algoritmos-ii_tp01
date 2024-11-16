import sys
sys.path.append('../src')

from trieCompacta import *

trie = TrieCompacta()
print("--- Trie Compacta ---")
print("Raiz:")
print(str(trie.raiz.chave) + ": " + str(trie.raiz.valor))

trie.raiz.filhos.append(No('by', 23))
trie.raiz.filhos.append(No('s'))
trie.raiz.filhos[1].filhos.append(No('he'))
trie.raiz.filhos[1].filhos[0].filhos.append(No('', 3))
trie.raiz.filhos[1].filhos[0].filhos.append(No('lls', 20))
trie.raiz.filhos[1].filhos.append(No('e'))
trie.raiz.filhos[1].filhos[1].filhos.append(No('a', [13, 31]))
trie.raiz.filhos[1].filhos[1].filhos.append(No('lls', 9))
trie.raiz.filhos.append(No('the', 27))

for i in range(0, trie.raiz.filhos.__len__()):
    print("Filho " + str(i) + ":")
    print(str(trie.raiz.filhos[i].chave) + ": " + str(trie.raiz.filhos[i].valor))
    if trie.raiz.filhos[i].filhos.__len__() > 0:
        for j in range(0, trie.raiz.filhos[i].filhos.__len__()):
            print("Filho " + str(i) + str(j) + ":")
            print(str(trie.raiz.filhos[i].filhos[j].chave) + ": " + str(trie.raiz.filhos[i].filhos[j].valor))
            if trie.raiz.filhos[i].filhos[j].filhos.__len__() > 0:
                for k in range(0, trie.raiz.filhos[i].filhos[j].filhos.__len__()):
                    print("Filho " + str(i) + str(j) +  str(k) + ":")
                    print(str(trie.raiz.filhos[i].filhos[j].filhos[k].chave) + ": " + str(trie.raiz.filhos[i].filhos[j].filhos[k].valor))


# Teste de Pesquisa 
print(trie.pesquisar("she"))
print(trie.pesquisar("sea"))
print(trie.pesquisar("coelho"))