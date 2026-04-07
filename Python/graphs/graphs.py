from collections import deque


def addEdge(adj: list[list], u: int, v: int) -> None:
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)

def create_adj(num_vert: int) -> list[list]:
    return [[] for _ in range(num_vert)]

def BFS(adj: list[list], source: int, visited: list[bool]) -> None:
    q = deque()
    q.append(source)

    visited[source] = True

    while q:
        s = q.popleft()
        print(s, end=" ")

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

def BFS_disconnected(adj: list[list]) -> None:
    visited = [False for _ in range(len(adj))]
    conn_comp = 0
    for u in range(len(adj)):
        if visited[u] == False:
            conn_comp += 1
            BFS(adj, u, visited)
    return conn_comp


if __name__ == "__main__":
    V = 4
    adj = create_adj(V)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    
    adj2 = [[1,2], [0,3], [0,3], [1,2], [5,6],[4,6],[4,5]]
    print(f"connected component equals {BFS_disconnected(adj2)}")