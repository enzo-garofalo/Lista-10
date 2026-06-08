# Análise Experimental de Algoritmos de Ordenação

Comparação experimental de três algoritmos de ordenação com complexidades de
pior caso diferentes, medindo tempo de execução e número de trocas/movimentações.

| Algoritmo | Caso médio | Pior caso | Operação contada |
|-----------|------------|-----------|------------------|
| Bubble Sort | O(n²) | O(n²) | trocas |
| Quick Sort | O(n log n) | O(n²) | trocas |
| Merge Sort | O(n log n) | O(n log n) | movimentações |



## Como rodar

### Testar um algoritmo isolado

Cada arquivo de algoritmo tem um exemplo próprio:

```bash
python3 bubble_sort.py
python3 quick_sort.py
python3 merge_sort.py
```

### Rodar o experimento completo

```bash
python3 ordenacao_experimento.py
```

Isso gera vetores aleatórios de **1.000, 10.000 e 100.000** elementos (o mesmo
vetor é usado por todos os algoritmos em cada tamanho), executa cada algoritmo
**3 vezes** e imprime tempos, média, desvio padrão e operações.
