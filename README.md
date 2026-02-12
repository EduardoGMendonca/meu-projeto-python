# Índice Remissivo com Árvore AVL

## Descrição

Este projeto implementa um **Índice Remissivo** utilizando uma **Árvore AVL** como estrutura de dados principal.

O sistema:

* Lê um arquivo texto (`texto_origem.txt`)
* Extrai e normaliza palavras
* Armazena palavras distintas em uma Árvore AVL
* Mantém a árvore automaticamente balanceada
* Registra as linhas onde cada palavra aparece
* Gera um arquivo de saída (`saida.txt`) com o índice ordenado
* Permite buscas e remoções
* Exibe estatísticas de execução

---

## Estrutura de Dados

A estrutura utilizada é uma **Árvore AVL**, que é uma árvore binária de busca auto-balanceada.

Cada nó da árvore armazena:

* `palavra` → string
* `linhas` → conjunto de linhas onde a palavra aparece
* `altura` → usada para cálculo do balanceamento
* `esq` → ponteiro para filho esquerdo
* `dir` → ponteiro para filho direito

A árvore mantém o fator de balanceamento sempre entre -1 e 1 por meio de rotações:

* Rotação LL
* Rotação RR
* Rotação LR
* Rotação RL

---

## Funcionalidades Implementadas

### Inserção

Insere palavras na árvore mantendo ordenação e balanceamento.

Se a palavra já existir:

* Incrementa a contagem
* Adiciona a linha (sem duplicar)

Complexidade: **O(log n)**

---

### Busca com ME (Margem de Equilíbrio)

Busca uma palavra e calcula:

```
ME = número de nós da subárvore esquerda − número de nós da subárvore direita
```

Retornos:

* `None` → palavra não encontrada
* Valor inteiro → diferença estrutural

Complexidade: **O(log n)**

---

### Busca por Prefixo

Retorna todas as palavras que começam com um determinado prefixo.

Complexidade: **O(n)**

---

### Remoção

Permite:

* Remover uma palavra de uma linha específica
* Se for a última linha → remove o nó da árvore
* Mantém balanceamento após remoção

Complexidade: **O(log n)**

---

### Palavra Mais Frequente

Retorna a palavra que aparece no maior número de linhas.

Complexidade: **O(n)**

---

### Geração do Índice

O arquivo `saida.txt` é gerado em ordem alfabética utilizando percurso **in-order** da AVL.

Formato:

```
palavra linha1,linha2,linha3
```

---

## Estatísticas Exibidas

Durante a execução são exibidos:

* Total de palavras lidas
* Total de palavras distintas
* Total de palavras descartadas (repetidas)
* Total de rotações executadas
* Tempo de processamento

---

## Como Executar

1. Coloque o arquivo `texto_origem.txt` na mesma pasta do projeto.
2. Execute:

```
python main.py
```

3. O índice será gerado em:

```
saida.txt
```

---

## Complexidade das Operações

| Operação               | Complexidade |
| ---------------------- | ------------ |
| Inserção               | O(log n)     |
| Remoção                | O(log n)     |
| Busca                  | O(log n)     |
| Busca por prefixo      | O(n)         |
| Palavra mais frequente | O(n)         |

---

## 🎯 Características Técnicas

* Implementação própria da Árvore AVL
* Balanceamento automático
* Controle explícito de rotações
* Estrutura totalmente dinâmica

---

## Testes Realizados

* Inserção crescente e decrescente (forçando rotações)
* Remoção de nós com:

  * 0 filhos
  * 1 filho
  * 2 filhos
* Inserções massivas
* Teste de estabilidade estrutural
* Teste de prefixo
* Teste de balanceamento (ME)

---

## Autores

Eduardo Gonçalves Mendonça
Gabriel Lima Araújo
