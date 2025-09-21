import sys


_INFINITY = sys.maxsize


def do_floyd_warshall_algorithm(
    adjacencies: list[dict[int, int]],
) -> list[list[int]]:
    n = len(adjacencies)
    distances = [[_INFINITY for _ in range(n)] for __ in range(n)]
    for u, neighbors in enumerate(adjacencies):
        distances[u][u] = 0
        for v, w in neighbors.items():
            distances[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                potential_distance = distances[i][k] + distances[k][j]
                distances[i][j] = min(distances[i][j], potential_distance)
    return distances
