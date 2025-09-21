import collections
import heapq
import sys


_INFINITY = sys.maxsize


def find_sssp_with_bfs(adjacencies: list[set[int]], source: int) -> list[int]:
    n = len(adjacencies)
    distances = [_INFINITY for _ in range(n)]
    distances[source] = 0
    queue = collections.deque()
    queue.append(source)
    while len(queue) > 0:
        u = queue.popleft()
        for v in adjacencies[u]:
            if distances[v] != _INFINITY:
                continue
            distances[v] = distances[u] + 1
            queue.append(v)
    return distances


def do_dfs_topological_sorting(adjacencies: list[set[int]]) -> list[int]:
    n = len(adjacencies)
    seen = set()
    reversed_nodes = list()
    def do_dfs(u: int) -> None:
        if u in seen:
            return
        seen.add(u)
        for v in adjacencies[u]:
            do_dfs(v)
        reversed_nodes.append(u)
    for u in range(n):
        do_dfs(u)
    sorted_nodes = reversed_nodes[::-1]
    return sorted_nodes


def do_one_pass_bellman_ford_algorithm(
    adjacencies: list[dict[int, int]],
    source: int,
) -> list[int]:
    n = len(adjacencies)
    distances = [_INFINITY for _ in range(n)]
    distances[source] = 0
    sorted_nodes = do_dfs_topological_sorting(adjacencies)
    for u in sorted_nodes:
        for v, w in adjacencies[u].items():
            if distances[u] >= _INFINITY or distances[u] + w >= distances[v]:
                continue
            distances[v] = distances[u] + w
    return distances


def do_dijkstras_algorithm(
    adjacencies: list[dict[int, int]],
    source: int,
) -> list[int]:
    n = len(adjacencies)
    distances = [_INFINITY for _ in range(n)]
    distances[source] = 0
    min_heap = list()
    heapq.heappush(min_heap, (distances[source], source))
    while len(min_heap) > 0:
        distance, u = heapq.heappop(min_heap)
        if distance > distances[u]:
            continue
        for v, w in adjacencies[u].items():
            potential_distance = distances[u] + w
            if distances[v] <= potential_distance:
                continue
            distances[v] = potential_distance
            heapq.heappush(min_heap, (potential_distance, v))
    return distances


def do_bellman_ford_algorithm(
    adjacencies: list[dict[int, int]],
    source: int,
) -> list[int]:
    n = len(adjacencies)
    distances = [_INFINITY for _ in range(n)]
    distances[source] = 0
    edges = list()
    for u, neighbors in enumerate(adjacencies):
        for v, w in neighbors.items():
            edge = u, v, w
            edges.append(edge)
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] == _INFINITY or distances[u] + w >= distances[v]:
                continue
            distances[v] = distances[u] + w
    return distances
