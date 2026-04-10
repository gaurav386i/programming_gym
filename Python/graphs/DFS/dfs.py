"""
Depth First Search()
Applications of DFS : 
1. Cycle Detection
2. Topological Sorting 
3. Strongly Connected Components
4. Solving Maze and similar puzzles
5. Path findings 
"""
from collections import deque

from utils import (
    INT_MAX, 
    generate_empty_adj, 
    generate_visited,
    add_list_of_edges
)


def DFS_Rec(adj: list[list], s: int, visited: list[bool]) -> None:
    visited[s] = True
    print(s, end=" ")

    for u in adj[s]:
        if visited[u] == False:
            DFS_Rec(adj, u, visited)


def DFS(adj: list[list], s: int) -> None:
    visited = [False for _ in range(len(adj))]
    DFS_Rec(adj, s, visited)


def DFS_disconected(adj: list[list]) -> None:
    visited = [False for _ in range(len(adj))]
    for u in range(len(adj)):
        if visited[u] == False:
            DFS_Rec(adj, u, visited)

"""
counting disconnected components in an undireted graph usig DFS .
"""
def count_disconected_comp_in_undir_graph(adj: list[list]) -> int:
    visited = [False for _ in range(len(adj))]

    count = 0
    for u in range(len(adj)):
        if visited[u] == False:
            count += 1
            DFS_Rec(adj, u, visited)
            
    return count

def get_shortest_path_from_source_each_vertices_bfs(
        adj: list[list], 
        s: int, 
        dist: list[int]
    ) -> None:
    visited = generate_visited(adj)
    q = deque()
    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()

        for v in adj[u]:
            if visited[v] == False:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.append(v)


def is_cycle_DFS_Rec(
        adj: list[list], 
        s: int, 
        visited: list[bool], 
        parent: int
    ) -> bool:
    visited[s] = True

    for u in adj[s]:
        if visited[u] == False:
            if is_cycle_DFS_Rec(adj, u, visited, s):
                return True
        elif u != parent:
            return True
    return False

def is_cycle_DFS(adj: list[list]) -> bool:
    visited = generate_visited(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            if is_cycle_DFS_Rec(adj, i, visited, -1):
                return True
    return False

def is_cyclic_graph(adj: list[list]) -> bool:
    if is_cycle_DFS(adj):
        print("Cycle found")
    else:
        print("No cycle found")

"""
10) Number of Islands

Topic: Graphs
Difficulty: Medium
Given a 2D grid of '1's and '0's, count the number of islands. 
An island is formed by connecting adjacent lands horizontally or vertically.
"""

def dfs_grid(grid: list[list],r: int, c: int):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
        return 
    grid[r][c] = 0
    dfs_grid(grid, r + 1, c)
    dfs_grid(grid, r - 1, c)
    dfs_grid(grid, r, c + 1)
    dfs_grid(grid, r, c - 1)

def find_num_islands(grid: list[list]) -> int:
    row = len(grid)
    col = len(grid[0])
    islands = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                islands += 1
                dfs_grid(grid, r, c)
    return islands


if __name__ == "__main__":
    V = 4
    adj = generate_empty_adj(V)
    add_list_of_edges(adj, [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3)])
    dist = [INT_MAX] * V
    dist[0] = 0
    get_shortest_path_from_source_each_vertices_bfs(adj, 0, dist)
    print(*dist)

    V1 = 6
    adj1 = generate_empty_adj(V1)
    
    add_list_of_edges(adj1, [(0,1), (1,2), (2,4), (4,5), (1,3), (2,3)])

    is_cyclic_graph(adj1)

    island_grid = [
        [1, 0, 0, 0, 1],
        [1, 1, 1 ,0, 0],
        [0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0]
    ]
    print("---++++++-------")
    print(find_num_islands(island_grid))
