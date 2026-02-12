from avl import AVL


def main():

    arv = AVL()

    print("Lendo arquivo...")
    arv.arquivo("texto_origem.txt")

    print("Gerando índice...")
    arv.arquivo_saida("saida.txt")

    print("\nBusca com ME:")
    resultado = arv.busca_com_me("de")

    if resultado is None:
        print("Palavra não encontrada.")
    else:
        print(f"ME = {resultado}")
        if abs(resultado) <= 1:
            print("Palavra encontrada e balanceada.")
        else:
            print("Palavra encontrada e desbalanceada.")

    print("\nBusca por prefixo 'alg':")
    print(arv.busca_prefixo("alg"))

    print("\nRemovendo palavra 'algoritmo' da linha 10...")
    arv.remover("algoritmo", 10)

    print("\nPalavra mais frequente:")
    palavra, qtd = arv.mais_frequente()
    print(f"'{palavra}' aparece em {qtd} linhas.")


if __name__ == "__main__":
    main()