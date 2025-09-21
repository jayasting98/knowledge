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


def transpose_graph(adjacencies: list[set[int]]) -> list[set[int]]:
    n = len(adjacencies)
    transposed_adjacencies = [set() for _ in range(n)]
    for u, neighbors in enumerate(adjacencies):
        for v in neighbors:
            transposed_adjacencies[v].add(u)
    return transposed_adjacencies


def do_kosarajus_algorithm(adjacencies: list[set[int]]) -> int:
    sorted_nodes = do_dfs_topological_sorting(adjacencies)
    transposed_adjacencies = transpose_graph(adjacencies)
    seen = set()
    def do_dfs(u: int) -> None:
        if u in seen:
            return
        seen.add(u)
        for v in transposed_adjacencies[u]:
            do_dfs(v)
    components_count = 0
    for u in sorted_nodes:
        if u in seen:
            continue
        components_count += 1
        do_dfs(u)
    return components_count
