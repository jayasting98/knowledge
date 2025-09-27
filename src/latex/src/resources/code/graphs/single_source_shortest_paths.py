import collections
import heapq

import constants
from graphs import topological_sorting


def find_sssp_with_bfs(adjacencies: list[set[int]], source: int) -> list[int]:
    n = len(adjacencies)
    distances = [constants.INFINITY for _ in range(n)]
    distances[source] = 0
    queue = collections.deque()
    queue.append(source)
    while len(queue) > 0:
        u = queue.popleft()
        for v in adjacencies[u]:
            if distances[v] < constants.INFINITY:
                continue
            distances[v] = distances[u] + 1
            queue.append(v)
    return distances


def do_one_pass_bellman_ford_algorithm(
    adjacencies: list[dict[int, int]],
    source: int,
) -> list[int]:
    n = len(adjacencies)
    distances = [constants.INFINITY for _ in range(n)]
    distances[source] = 0
    sorted_nodes = topological_sorting.do_dfs_topological_sorting(adjacencies)
    for u in sorted_nodes:
        for v, w in adjacencies[u].items():
            if distances[u] >= constants.INFINITY:
                continue
            potential_distance = distances[u] + w
            if potential_distance >= distances[v]:
                continue
            distances[v] = potential_distance
    return distances


def do_dijkstras_algorithm(
    adjacencies: list[dict[int, int]],
    source: int,
) -> list[int]:
    n = len(adjacencies)
    distances = [constants.INFINITY for _ in range(n)]
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
    distances = [constants.INFINITY for _ in range(n)]
    distances[source] = 0
    edges = list()
    for u, neighbors in enumerate(adjacencies):
        for v, w in neighbors.items():
            edge = u, v, w
            edges.append(edge)
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] >= constants.INFINITY:
                continue
            potential_distance = distances[u] + w
            if potential_distance >= distances[v]:
                continue
            distances[v] = potential_distance
    return distances
