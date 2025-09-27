import constants


def do_floyd_warshall_algorithm(
    adjacencies: list[dict[int, int]],
) -> list[list[int]]:
    n = len(adjacencies)
    distances = [[constants.INFINITY for _ in range(n)] for __ in range(n)]
    for u, neighbors in enumerate(adjacencies):
        distances[u][u] = 0
        for v, w in neighbors.items():
            distances[u][v] = w
    for k in range(n):
        for i in range(n):
            if distances[i][k] >= constants.INFINITY:
                continue
            for j in range(n):
                if distances[k][j] >= constants.INFINITY:
                    continue
                potential_distance = distances[i][k] + distances[k][j]
                distances[i][j] = min(distances[i][j], potential_distance)
    return distances
