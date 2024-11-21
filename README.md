# Algoritmos II - TP01 - Manipulação de Sequências

### **Alunos:** Marcos Paulo Ferreria de Souza, Christian David Costa Vieira

## Introdução

Este relatório apresenta a implementação de um algoritmo de compressão e de uma estrutura de dados. O algoritmo de compressão elaborado é o LZW, que funciona identificando os padrões repetidos em um arquivo e os substituindo por identificadores únicos, gerando assim uma versão comprimida do arquivo. A Trie Compacta, usada para otimizar a compressão, é uma estrutura de dados que armazena de maneira eficiente e compacta os padrões e identificadores gerados pelo algoritmo.

## Implementação

Para realizar a implementação foi utilizado a linguagem de programação Python. Quatro arquivos distintos foram criados para organizar e facilitar a escrita do programa. O arquivo que será executado é o “main.py” que processa as entradas e chama o “lzw.py” que realiza a compressão.A leitura do arquivo de entrada é feita utilizando o “io_manip.py” e o “trieCompacta.py” é usado para armazenar os padrões e os identificadores usados na compressão e a descompressão. A lógica e as decisões que foram feitas na escrita dos códigos “lzw.py” e o “trieCompacta.py” serão explicados nas próximas seções.

## LZW

O algoritmo de compressão foi implementado no arquivo “lzw.py”. O funcionamento do algoritmo se dá pela leitura dos bytes do arquivo de entrada e pela associação desses bytes a identificadores que serão registrados no arquivo comprimido. Sendo que os bytes são associados em sequências que se repetem ao longo do arquivo, ou seja, uma sequência de bytes possui um identificador único e sempre que essa sequência se repetir no arquivo ela será substituída pelo mesmo identificador. Os identificadores associados a apenas uma sequência garante que a compressão seja reversível. A descompressão segue a mesma lógica mas de forma inversa, todo identificador lido do arquivo é traduzido pelo padrão que ele identifica, assim reconstruindo o arquivo original.

## Trie Compacta

A Trie Compacta foi implementada como uma árvore composta por nós que possuem apenas três campos, a chave, o valor e uma lista de nós filhos. Por definição, a Trie Compacta é uma árvore de prefixos, por tanto cada nó vai ter como chave o maior prefixo compartilhado entre os seus nós filhos e apenas as folhas vão possuir valores. Seguindo essas definições foram implementadas as funções de inserção, remoção e pesquisa de chaves na árvore. Caso a mesma chave seja inserida mais de uma vez, ela irá possuir como os seus N primeiros filhos, sendo N o número de vezes que a chave foi inserida na árvore, nós com a chave vazia e que possuem os valores associados a chave nas diferentes inserções. Caso uma chave que foi inserida mais de uma vez seja removida todos os valores associados a ela serão removidos, ou seja, independentemente de quantas vezes uma chave foi inserida na árvore ao ser removido todos os valores associados a ela serão retirados da árvore.

## Resultados

Foram feitos dois testes, o primeiro com um arquivo .txt com 4.2 MB e o segundo com um arquivo .tiff com 0.85 MB. Os arquivos foram comprimidos com uma taxa de compressão no melhor caso de 3.00, comparável com implementações padrões como a do gzip. A descompressão foi feita com sucesso retornando o mesmo arquivo que foi passado na entrada do algoritmo.

| Compressor | Algoritmo        | Arquivo        | Num de bits  | Razão de Compressão (%) | 
| ---------- | ---------------- | -------------- | ------------ | ----------------------- | 
| gzip       | LZW + Huffman    | BIBLIA.txt     |              |  3.00                   | 
| tp01-lzw   | LZW              | BIBLIA.txt     | 9            |  1.35                   | 
| tp01-lzw   | LZW              | BIBLIA.txt     | 12           |  2.10                   | 
| tp01-lzw   | LZW              | BIBLIA.txt     | 15           |  2.47                   | 
| tp01-lzw   | LZW              | BIBLIA.txt     | 18           |  3.00                   |
| tp01-lzw   | LZW              | BIBLIA.txt     | 20           |  3.00                   |
| tp01-lzw   | LZW              | BIBLIA.txt     | sem limite   |  3.00                   |

A Figura abaixo exibe o gráfico com a razão de compressão para o arquivo .txt BIBLIA.txt de 4.2MB. Pode-se observar que com a quantidade de bits elevada, a taxa aproxima-se da taxa obtida de compactadores padrões amplamente utilizado, como é o caso do gzip.

<img title="Razão de Compressão" src="/doc/razao-de-compressao-biblia.png">

## Melhorias
O tempo para compressão e descompressão utilizando árvore Trie Compacta foi muito além do esperado, demorando cerca de 7.5 min. em média para compressão e descompressão! O tempo elevado se deu em razão de cada valor do nodo da árvore Trie Compacta ser armazenado em uma lista. Verificando outras possibilidades de containers, pode-se perceber que o do tipo dicionário seria o mais adequado para esse caso. Testes iniciais realizados mostraram-se promissores, mas devido ao tempo necessário para reescrever e debug completo, não foi possível completar a refatoração.

Um outro caso que poderá ser melhorado consiste na leitura de chuncks do arquivo de entrada e escrita de chunks no arquivo de saída, tendo como base a informação disposnibilizada pelo OS acerca da geometria do disco (memória de massa). Isso de certo modo poderia trazer impactos positivos no caso de arquivos muito grandes.

Acerca de boas práticas de engenharia de software, a adoção de padrões de projeto como o Template poderia ser benéfico para extender a possibilidade de avaliações de outras implementações de containers (neste contexto, container é a implementação que contém os dados do arquivo de compressão/descompressão), como é o caso exposto anteriormente para avaliação de uma estrutura de dados para armazenamento dos valores dos nós ou mesmo avaliações de outros tipos de estruturas do tipo Tries .

## Conclusão

A implementação do algoritmo de compressão LZW e da Trie Compacta demonstrou ser uma solução eficiente para a compressão e descompressão de arquivos. O uso da Trie Compacta otimizou o armazenamento e a manipulação dos padrões repetidos, enquanto o LZW garantiu uma compressão reversível e competitiva em termos de taxa de compressão, conforme evidenciado pelos testes realizados.

Os resultados obtidos mostraram que a taxa de compressão alcançada é comparável a padrões amplamente utilizados, como o gzip, especialmente quando a quantidade de bits é elevada. Isso destaca o potencial da solução proposta para aplicações práticas em contextos que exigem compressão eficiente e confiável.

Por fim, a modularidade do código, organizada em arquivos distintos, contribuiu para a clareza e manutenção do projeto, facilitando futuras expansões ou ajustes. Esta abordagem reforça o sucesso da implementação, tanto em aspectos técnicos quanto em organização de software.