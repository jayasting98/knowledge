import heapq
from typing import Self


def do_prims_algorithm(adjacencies: list[dict[int, int]]) -> list[dict[int, int]]:
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


class Ufds:
    def __init__(self: Self, n: int) -> None:
        self._parents = list(range(n))
        self._ranks = [0 for _ in range(n)]

    def find(self: Self, x: int) -> int:
        if self._parents[x] != x:
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def union(self: Self, x: int, y: int) -> None:
        set_x = self.find(x)
        set_y = self.find(y)
        if set_x == set_y:
            return
        if self._ranks[set_y] > self._ranks[set_x]:
            self._parents[set_x] = set_y
        else:
            self._parents[set_y] = set_x
            if self._ranks[set_x] == self._ranks[set_y]:
                self._ranks[set_x] += 1


def do_kruskals_algorithm(adjacencies: list[dict[int, int]]) -> list[dict[int, int]]:
    n = len(adjacencies)
    edges = list()
    for u, neighbors in enumerate(adjacencies):
        for v, w in neighbors.items():
            edge = w, u, v
            edges.append(edge)
    edges.sort()
    mst_adjacencies = [dict() for _ in range(n)]
    ufds = Ufds(n)
    for w, u, v in edges:
        if ufds.find(u) == ufds.find(v):
            continue
        ufds.union(u, v)
        mst_adjacencies[u][v] = w
        mst_adjacencies[v][u] = w
    return mst_adjacencies
