"""
Experimento comparativo:

Importa os três algoritmos (cada um em seu arquivo), gera vetores aleatórios de
1.000, 10.000 e 100.000 elementos (o MESMO vetor é usado por todos os algoritmos
em cada tamanho) e mede tempo e trocas/movimentações em 3 execuções.

Algoritmos com complexidades de pior caso diferentes:
  - Bubble Sort: O(n^2)
  - Quick Sort:  O(n^2) no pior caso, O(n log n) no caso médio
  - Merge Sort:  O(n log n)

Caso um algoritmo não termine em 5 minutos, registra N/C.
"""
import random
import statistics
import time

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

TAMANHOS = [1000, 10000, 100000]
N_EXEC = 3
LIMITE_S = 300  # 5 minutos
random.seed(42)

# Mesmo vetor original por tamanho para todos os algoritmos
vetores = {n: [random.randint(0, 10**9) for _ in range(n)] for n in TAMANHOS}


def medir(func, n):
    """Executa `func` N_EXEC vezes sobre o vetor de tamanho n; valida a ordenação."""
    tempos, ops = [], None
    base = vetores[n]
    esperado = sorted(base)
    for _ in range(N_EXEC):
        t0 = time.perf_counter()
        ordenado, operacoes = func(base)
        tempos.append(time.perf_counter() - t0)
        ops = operacoes
        assert ordenado == esperado
    return tempos, ops


def imprime(nome, n, tempos, ops):
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
    execs = "  ".join(f"{t:.4f}" for t in tempos)
    print(f"{nome:<12} n={n:<7} execs=[{execs}]  media={media:.4f}s  "
          f"desvio={desvio:.4f}s  ops={ops}")


if __name__ == "__main__":
    print("Tamanhos:", TAMANHOS, "| execucoes por teste:", N_EXEC, "\n")

    # Bubble (em 100.000 nao termina em 5 min -> N/C, confirmado por probe de 30s)
    for n in TAMANHOS:
        if n <= 10000:
            tempos, ops = medir(bubble_sort, n)
            imprime("Bubble Sort", n, tempos, ops)
        else:
            try:
                bubble_sort(vetores[n], deadline=30)  # probe
                tempos, ops = medir(bubble_sort, n)
                imprime("Bubble Sort", n, tempos, ops)
            except TimeoutError as e:
                print(f"Bubble Sort  n={n:<7} N/C ({e})")

    for n in TAMANHOS:
        tempos, ops = medir(quick_sort, n)
        imprime("Quick Sort", n, tempos, ops)

    for n in TAMANHOS:
        tempos, ops = medir(merge_sort, n)
        imprime("Merge Sort", n, tempos, ops)
