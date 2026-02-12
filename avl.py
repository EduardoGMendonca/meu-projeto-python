import re
import time
from no import NO


class AVL:

    def __init__(self):
        self.__raiz = None
        self.__descartadas = 0
        self.__rotacoes = 0
        self.__tempo = 0

    def __altura(self, no):
        return -1 if no is None else no.altura

    def __maior(self, x, y):
        return x if x > y else y

    def __fator(self, no):
        return self.__altura(no.esq) - self.__altura(no.dir)

    def __rotacaoLL(self, A):
        self.__rotacoes += 1
        B = A.esq
        A.esq = B.dir
        B.dir = A

        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), self.__altura(B.dir)) + 1

        return B

    def __rotacaoRR(self, A):
        self.__rotacoes += 1
        B = A.dir
        A.dir = B.esq
        B.esq = A

        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), self.__altura(B.dir)) + 1

        return B

    def __rotacaoLR(self, A):
        A.esq = self.__rotacaoRR(A.esq)
        return self.__rotacaoLL(A)

    def __rotacaoRL(self, A):
        A.dir = self.__rotacaoLL(A.dir)
        return self.__rotacaoRR(A)

    def __insere(self, atual, palavra, linha):

        if atual is None:
            novo = NO(palavra)
            novo.linhas.append(linha)
            return novo

        if palavra < atual.info:
            atual.esq = self.__insere(atual.esq, palavra, linha)

        elif palavra > atual.info:
            atual.dir = self.__insere(atual.dir, palavra, linha)

        else:
            atual.quantidade += 1
            self.__descartadas += 1

            if linha not in atual.linhas:
                atual.linhas.append(linha)

            return atual

        atual.altura = self.__maior(
            self.__altura(atual.esq),
            self.__altura(atual.dir)
        ) + 1

        fator = self.__fator(atual)

        if fator > 1:
            if palavra < atual.esq.info:
                return self.__rotacaoLL(atual)
            else:
                return self.__rotacaoLR(atual)

        if fator < -1:
            if palavra > atual.dir.info:
                return self.__rotacaoRR(atual)
            else:
                return self.__rotacaoRL(atual)

        return atual

    def inserir(self, palavra, linha):
        self.__raiz = self.__insere(self.__raiz, palavra, linha)

    def __menor_valor(self, no):
        atual = no
        while atual.esq:
            atual = atual.esq
        return atual

    def __remove(self, atual, palavra):

        if atual is None:
            return atual

        if palavra < atual.info:
            atual.esq = self.__remove(atual.esq, palavra)

        elif palavra > atual.info:
            atual.dir = self.__remove(atual.dir, palavra)

        else:
            if atual.esq is None:
                return atual.dir

            elif atual.dir is None:
                return atual.esq

            temp = self.__menor_valor(atual.dir)

            atual.info = temp.info
            atual.linhas = temp.linhas
            atual.quantidade = temp.quantidade

            atual.dir = self.__remove(atual.dir, temp.info)

        atual.altura = self.__maior(
            self.__altura(atual.esq),
            self.__altura(atual.dir)
        ) + 1

        fator = self.__fator(atual)

        if fator > 1:
            if self.__fator(atual.esq) >= 0:
                return self.__rotacaoLL(atual)
            else:
                return self.__rotacaoLR(atual)

        if fator < -1:
            if self.__fator(atual.dir) <= 0:
                return self.__rotacaoRR(atual)
            else:
                return self.__rotacaoRL(atual)

        return atual

    def remover(self, palavra, linha):

        no = self.__buscar_no(self.__raiz, palavra)

        if no is None:
            return False

        if linha in no.linhas:
            no.linhas.remove(linha)

        if len(no.linhas) == 0:
            self.__raiz = self.__remove(self.__raiz, palavra)

        return True

    def __buscar_no(self, atual, palavra):

        while atual:
            if palavra == atual.info:
                return atual
            elif palavra < atual.info:
                atual = atual.esq
            else:
                atual = atual.dir

        return None

    def busca(self, palavra):
        no = self.__buscar_no(self.__raiz, palavra)
        return None if no is None else sorted(no.linhas)

    def __contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self.__contar_nos(no.esq) + self.__contar_nos(no.dir)

    def busca_com_me(self, palavra):
        no = self.__buscar_no(self.__raiz, palavra)

        if no is None:
            return None

        altura_esq = no.esq.altura if no.esq else 0
        altura_dir = no.dir.altura if no.dir else 0

        return altura_esq - altura_dir

    def busca_prefixo(self, prefixo):
        resultado = []
        self.__prefixo(self.__raiz, prefixo.lower(), resultado)
        return resultado

    def __prefixo(self, no, prefixo, resultado):
        if no:
            self.__prefixo(no.esq, prefixo, resultado)

            if no.info.startswith(prefixo):
                resultado.append(no.info)

            self.__prefixo(no.dir, prefixo, resultado)

    def arquivo(self, nome):
        inicio = time.time()

        with open(nome, "r", encoding="utf-8") as arq:
            linha_num = 0

            for linha in arq:
                linha_num += 1
                palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", linha.lower())

                for p in palavras:
                    self.inserir(p, linha_num)

        self.__tempo = time.time() - inicio

    def __em_ordem(self, no, lista):
        if no:
            self.__em_ordem(no.esq, lista)
            lista.append((no.info, no.quantidade, no.linhas))
            self.__em_ordem(no.dir, lista)

    def arquivo_saida(self, nome_saida):

        elementos = []
        self.__em_ordem(self.__raiz, elementos)

        total_palavras = sum(e[1] for e in elementos)
        distintas = len(elementos)

        with open(nome_saida, "w", encoding="utf-8") as arq:

            for palavra, qtd, linhas in elementos:
                linhas_str = ",".join(map(str, sorted(linhas)))
                arq.write(f"{palavra} {linhas_str}\n")

            arq.write("\n")
            arq.write(f"Total de palavras: {total_palavras}\n")
            arq.write(f"Total de palavras distintas: {distintas}\n")
            arq.write(f"Total de palavras descartadas: {self.__descartadas}\n")
            arq.write(f"Tempo de construção do índice usando árvore AVL: {self.__tempo:.4f}s\n")
            arq.write(f"Total de rotações executadas: {self.__rotacoes}\n")

    def mais_frequente(self):
        return self.__mais_frequente(self.__raiz)

    def __mais_frequente(self, no):

        if no is None:
            return ("", 0)

        esq = self.__mais_frequente(no.esq)
        dir = self.__mais_frequente(no.dir)
        atual = (no.info, len(no.linhas))

        return max(atual, esq, dir, key=lambda x: x[1])
