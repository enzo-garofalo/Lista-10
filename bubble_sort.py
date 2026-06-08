"""
Bubble Sort

Complexidade de tempo: O(n^2) no caso médio e no pior caso; O(n) no melhor
caso (vetor já ordenado, com a otimização da flag 'troquei').
Complexidade de espaço: O(1).

Conta o número de trocas (quando dois elementos mudam de posição).
"""
import time


def bubble_sort(lista, deadline=None):
    """Ordena uma cópia de `lista` e retorna (lista_ordenada, numero_de_trocas).

    Se `deadline` (em segundos) for informado e for ultrapassado, levanta
    TimeoutError — útil para interromper execuções muito longas.
    """
    a = lista[:]
    trocas = 0
    n = len(a)
    inicio = time.perf_counter()

    for i in range(n - 1):
        troquei = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trocas += 1
                troquei = True
        # se nenhuma troca ocorreu nesta passagem, o vetor já está ordenado
        if not troquei:
            break
        if deadline is not None and (time.perf_counter() - inicio) > deadline:
            raise TimeoutError(f"Bubble Sort abortado após {deadline}s (passagem {i}/{n})")

    return a, trocas


if __name__ == "__main__":
    exemplo = [5, 2, 9, 1, 5, 6]
    ordenado, trocas = bubble_sort(exemplo)
    print("Original:", exemplo)
    print("Ordenado:", ordenado)
    print("Trocas:  ", trocas)
