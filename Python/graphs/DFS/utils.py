INT_MAX = 4294967296

def addEdge(adj: list[list], u: int, v: int) -> None:
    adj[u].append(v)
    adj[v].append(u)


def add_list_of_edges(adj: list[list], edges: list[tuple[int]]) -> None:
    for u,v in edges:
        addEdge(adj, u, v)


def generate_empty_adj(size: int) -> list[list]:
    return [[] for _ in range(size)]

def generate_visited(adj: list[list]) -> list[bool]:
    return [False for _ in range(len(adj))]

