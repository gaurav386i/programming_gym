def printGraph(V: int, edges: list[list[int]]) -> list[list[int]]:
    if not V or not edges:
        return []
    graph = {i: [] for i in range(V)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return list(graph.values())


print(printGraph(5, [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]))