import heapq

import ufds


def do_prims_algorithm(
    adjacencies: list[dict[int, int]],
) -> list[dict[int, int]]:
    n = len(adjacencies)
    seen = {0}
    min_heap: list[tuple[int, int, int]] = list()
    for v, w in adjacencies[0].items():
        heapq.heappush(min_heap, (w, v, 0))
    mst_adjacencies = [dict() for _ in range(n)]
    while len(min_heap) > 0:
        w, v, u = heapq.heappop(min_heap)
        if v in seen:
            continue
        seen.add(v)
        mst_adjacencies[u][v] = w
        mst_adjacencies[v][u] = w
        for x, c in adjacencies[v].items():
            heapq.heappush(min_heap, (c, x, v))
    return mst_adjacencies


def do_kruskals_algorithm(
    adjacencies: list[dict[int, int]],
) -> list[dict[int, int]]:
    n = len(adjacencies)
    edges = list()
    for u, neighbors in enumerate(adjacencies):
        for v, w in neighbors.items():
            edge = w, u, v
            edges.append(edge)
    edges.sort()
    mst_adjacencies = [dict() for _ in range(n)]
    trees = ufds.Ufds(n)
    for w, u, v in edges:
        if trees.find(u) == trees.find(v):
            continue
        trees.union(u, v)
        mst_adjacencies[u][v] = w
        mst_adjacencies[v][u] = w
    return mst_adjacencies
