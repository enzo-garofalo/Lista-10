"""
Quick Sort
----------
Complexidade de tempo: O(n log n) no caso médio; O(n^2) no pior caso (raro com
pivô aleatório). Complexidade de espaço: O(log n) em média (pilha de recursão).

Usa pivô aleatório (reduz a chance do pior caso) e recorre sempre no lado menor,
iterando no maior, para manter a profundidade da pilha em O(log n).
Conta o número de trocas (quando dois elementos mudam de posição).
"""
import random
import sys

sys.setrecursionlimit(400000)


def quick_sort(lista):
    """Ordena uma cópia de `lista` e retorna (lista_ordenada, numero_de_trocas)."""
    a = lista[:]
    trocas = [0]

    def _qs(lo, hi):
        while lo < hi:
            # pivô aleatório levado para o fim
            p = random.randint(lo, hi)
            if p != hi:
                a[p], a[hi] = a[hi], a[p]
                trocas[0] += 1
            pivo = a[hi]

            # particionamento (Lomuto)
            i = lo
            for j in range(lo, hi):
                if a[j] < pivo:
                    if i != j:
                        a[i], a[j] = a[j], a[i]
                        trocas[0] += 1
                    i += 1
            if i != hi:
                a[i], a[hi] = a[hi], a[i]
                trocas[0] += 1

            # recorre no lado menor, itera no maior (profundidade O(log n))
            if i - lo < hi - i:
                _qs(lo, i - 1)
                lo = i + 1
            else:
                _qs(i + 1, hi)
                hi = i - 1

    if a:
        _qs(0, len(a) - 1)
    return a, trocas[0]


if __name__ == "__main__":
    exemplo = [5, 2, 9, 1, 5, 6]
    ordenado, trocas = quick_sort(exemplo)
    print("Original:", exemplo)
    print("Ordenado:", ordenado)
    print("Trocas:  ", trocas)
