# algoritmos-ii_tp01
Algoritmos II - TP01 - Manipulação de Sequências

### Executando testes:

Para executar os teste entre na pasta ./test pelo terminal e execute o comando 

> python3 < nome-do-arquivo-de-teste >

### Convenções de commit:

https://medium.com/linkapi-solutions/conventional-commits-pattern-3778d1a1e657



## 

No OS GNU/Linux, diversos utilitários de compressão utilizam  *LZW (Lempel-Ziv-Welch)* ou variantes do algoritmo *LZW*. Abaixo estão alguns dos compressores mais conhecidos:

| Compressor/Descompressor | Algoritmo                     | Extensão   | Comando de Compressão      | Comando de Descompressão      |
|--------------------------|-------------------------------|------------|----------------------------|-------------------------------|
| gzip                     | LZW + Huffman                 | `.gz`      | `gzip arquivo.txt`         | `gunzip arquivo.txt.gz`       |
| compress                 | LZW                           | `.Z`       | `compress arquivo.txt`     | `uncompress arquivo.txt.Z`    |
| xz                       | LZMA (LZ77 variante)          | `.xz`      | `xz arquivo.txt`           | `unxz arquivo.txt.xz`         |
| lzma                     | LZ77                          | `.lzma`    | `lzma arquivo.txt`         | `unlzma arquivo.txt.lzma`     |
| lzip                     | LZMA                          | `.lz`      | `lzip arquivo.txt`         | `unlzip arquivo.txt.lz`       |
| p7zip                    | LZMA/LZ77/LZW                 | `.7z`      | `7z a arquivo.7z arquivo`  | `7z x arquivo.7z`             |
| bzip2                    | Burrows-Wheeler + Huffman     | `.bz2`     | `bzip2 arquivo.txt`        | `bunzip2 arquivo.txt.bz2`     |
| lrzip                    | LZ77 + otimizações            | `.lrz`     | `lrzip arquivo.txt`        | `lrunzip arquivo.txt.lrz`     |
| lz4                      | LZ77 (compressão rápida)      | `.lz4`     | `lz4 arquivo.txt`          | `unlz4 arquivo.txt.lz4`       |
| zstd                     | LZ77 + Huffman                | `.zst`     | `zstd arquivo.txt`         | `unzstd arquivo.txt.zst`      |
| rar/unrar                | LZ77                          | `.rar`     | `rar a arquivo.rar arquivo`| `unrar x arquivo.rar`         |
| cpio                     | Vários (combinado com gzip)   | `.cpio`    | `cpio -o > arquivo.cpio`   | `cpio -i < arquivo.cpio`      |
| ar                       | Nenhum (empacotador)          | `.a`       | `ar r arquivo.a arquivos`  | `ar x arquivo.a`              |


### Considerações:
**Licenciamento e patentes:** O algoritmo *LZW* foi patenteado, e algumas implementações do *LZW* (como o compress) podem ter questões relacionadas a licenciamento devido a essas patentes. Isso fez com que alternativas como gzip e xz, que usam variantes do LZ77 ou LZMA, se tornassem mais populares.

**Desempenho e Taxa de Compressão:** Ferramentas como gzip e xz geralmente oferecem um bom equilíbrio entre desempenho de compressão/descompressão e taxa de compressão, enquanto outras como lzma e 7zip podem atingir taxas de compressão mais altas, mas com um custo de maior uso de CPU e tempo de processamento.

Esses algoritmos são amplamente utilizados no ecossistema Linux e Unix para compressão de arquivos, cada um com suas características de desempenho e adequação a diferentes cenários de uso.