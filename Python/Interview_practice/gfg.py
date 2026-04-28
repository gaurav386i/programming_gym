def printGraph(V: int, edges: list[list[int]]) -> list[list[int]]:
    if not V or not edges:
        return []
    graph = {i: [] for i in range(V)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return list(graph.values())


def star_triangel(n):
    # 10
    k = n-1
    for i in range(0, n):
        for j in range(k):
            print(end=" ")
        k = k-1
        for j in range(i+1):
            print("* ", end="")
        print(end="\n")


star_triangel(10)