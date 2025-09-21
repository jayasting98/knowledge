import collections


def do_kahns_algorithm(adjacencies: list[set[int]]) -> list[int]:
    n = len(adjacencies)
    indegrees = [0 for _ in range(n)]
    for neighbors in adjacencies:
        for v in neighbors:
            indegrees[v] += 1
    queue = collections.deque()
    for u, indegree in enumerate(indegrees):
        if indegree < 1:
            queue.append(u)
    sorted_nodes = list()
    while len(queue) > 0:
        u = queue.popleft()
        sorted_nodes.append(u)
        for v in adjacencies[u]:
            if indegrees[v] > 0:
                indegrees[v] -= 1
                continue
            queue.append(v)
    return sorted_nodes


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
