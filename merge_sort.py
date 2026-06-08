"""
Merge Sort
----------
Complexidade de tempo: O(n log n) no melhor, médio e pior caso (garantido).
Complexidade de espaço: O(n) (vetores auxiliares na intercalação).

Conta o número de movimentações (cada elemento escrito no vetor resultante
durante a intercalação conta como uma movimentação).
"""


def merge_sort(lista):
    """Ordena `lista` e retorna (lista_ordenada, numero_de_movimentacoes)."""
    movimentacoes = [0]

    def _ms(arr):
        if len(arr) <= 1:
            return arr
        meio = len(arr) // 2
        esq = _ms(arr[:meio])
        dir = _ms(arr[meio:])

        # intercalação
        res = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            if esq[i] <= dir[j]:
                res.append(esq[i]); i += 1
            else:
                res.append(dir[j]); j += 1
            movimentacoes[0] += 1
        while i < len(esq):
            res.append(esq[i]); i += 1; movimentacoes[0] += 1
        while j < len(dir):
            res.append(dir[j]); j += 1; movimentacoes[0] += 1
        return res

    return _ms(lista[:]), movimentacoes[0]


if __name__ == "__main__":
    exemplo = [5, 2, 9, 1, 5, 6]
    ordenado, mov = merge_sort(exemplo)
    print("Original:     ", exemplo)
    print("Ordenado:     ", ordenado)
    print("Movimentações:", mov)
