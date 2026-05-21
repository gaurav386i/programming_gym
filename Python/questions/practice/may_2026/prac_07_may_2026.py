from collections import deque

from utils import TreeNode, create_bt, print_output

"""
---

# Set 1

## 1) Same Tree

**Difficulty:** Easy

Given the roots of two binary trees `p` and `q`, write 
a function to check if they are the same.

Two binary trees are considered the same if they are 
structurally identical, and the nodes have the same value.

### Example

**Input:**
`p = [1,2,3], q = [1,2,3]`
**Output:**
`true`

---
"""


@print_output
def is_same_bt(p: TreeNode, q:TreeNode) -> bool:
    if p is None or q is None:
        return False
    st = [(p, q)]
    while st:
        n1, n2 = st.pop()
        if n1 is None and n2 is None:
            continue
        if n1 is None or n2 is None:
            return False
        if n1.key != n2.key:
            return False
    
        st.append((n1.left, n2.left))
        st.append((n1.right, n2.right))
    return True


p = create_bt([1,2,3])
q = create_bt([1,2,3])

# is_same_bt(p, q)
"""

## 2) Maximum Depth of Binary Tree

**Difficulty:** Easy

Given the `root` of a binary tree, return its maximum depth.

A binary tree’s maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`3`

---

"""


@print_output
def max_depth_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return max(
            max_depth_bt(root.left), max_depth_bt(root.right)
        ) + 1
    

@print_output
def max_depth_bt_itr(root: TreeNode) -> int:
    st = [(root, 1)]
    max_depth = 0
    while st:
        node, depth = st.pop()
        max_depth = max(max_depth, depth)
        if node.left:
            st.append((node.left, depth + 1))
        if node.right:
            st.append((node.right, depth + 1))
    return max_depth


# bt1 = create_bt([3,9,20,None,None,15,7])
# max_depth_bt_itr(bt1)

"""

## 3) Find if Path Exists in Graph

**Difficulty:** Easy

There is a bi-directional graph with `n` vertices. 
Determine whether there is a valid path from `source` to `destination`.

### Example

**Input:**
`n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2`
**Output:**
`true`

---
"""


@print_output
def path_exists_in_graph(
        n: int, 
        edges: list[list[int]], 
        source: int, 
        destination: int
) -> bool:
    if source == destination:
        return True
    graph = [[] for i in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q = deque([source])
    visited = [False] * n
    visited[source] = True
    while q:
        curr_node = q.popleft()

        for nei in graph[curr_node]:
            if nei == destination:
                return True
            if visited[nei] == False:
                visited[nei] == True
                q.append(nei)
    return False



"""

## 4) Binary Tree Level Order Traversal

**Difficulty:** Medium

Given the `root` of a binary tree, return the level order traversal 
of its nodes’ values.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[9,20],[15,7]]`

---

"""


@print_output
def level_order_traversal(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    q = deque([root])
    resp = []

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        resp.append(level)
    
    return resp
"""

## 5) Number of Islands

**Difficulty:** Medium

Given an `m x n` 2D binary grid `grid` of `'1'`s and `'0'`s, 
return the number of islands.

### Example

**Input:**
`grid = [["1","1","0"],["1","1","0"],["0","0","1"]]`
**Output:**
`2`

---
"""
def dfs(mat: list[list[int]], r: int, c: int) -> None:
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] == "0":
        return
    directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
    mat[r][c] = "0"

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        dfs(mat, nr, nc)


@print_output
def num_islands(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0
    
    rows = len(mat)
    cols = len(mat[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == "1":
                count += 1
                dfs(mat, r, c)
    return count


"""

## 6) Course Schedule

**Difficulty:** Medium

There are `numCourses` courses you have to take, 
labeled from `0` to `numCourses - 1`.

You are given an array `prerequisites` where 
`prerequisites[i] = [a, b]` indicates that you 
must take course `b` first if you want to take course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`true`

---

"""

@print_output
def can_pass_all_courses(numCourses: int, prerequisites: list[list[int]]) -> bool:
    if not numCourses or not prerequisites:
        return False
    graph = {i: [] for i in range(numCourses)}
    indegrees = [0] * numCourses
    q = deque()
    for c, p in prerequisites:
        graph[p].append(c)
        indegrees[c] += 1
    for c in graph:
        if indegrees[c] == 0:
            q.append(c)
    count = 0

    while q:
        n = q.popleft()
        count += 1
        for nei in graph[n]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    
    return True if count == numCourses else False

"""

## 7) Jump Game

**Difficulty:** Medium

You are given an integer array `nums`. Each element represents 
your maximum jump length at that position.

Return `true` if you can reach the last index, 
or `false` otherwise.

### Example

**Input:**
`nums = [2,3,1,1,4]`
**Output:**
`true`

---
"""


@print_output
def jump_game(nums: list[int]) -> bool:
    if not nums:
        return False
    
    max_reachable = 0
    n = len(nums)
    
    for i in range(n):
        # If the current index is beyond our 
        # furthest reachable point, we're stuck
        if i > max_reachable:
            return False
        
        # Update our horizon: can we get 
        # further from here?
        max_reachable = max(max_reachable, i + nums[i])
        
        # Optimization: if the horizon already 
        # covers the last index, we're done
        if max_reachable >= n - 1:
            return True
            
    return max_reachable >= n - 1



"""

## 8) Queue Reconstruction by Height

**Difficulty:** Medium

You are given an array `people` where 
`people[i] = [hi, ki]` represents the `i`th person.

Reconstruct and return the queue.

### Example

**Input:**
`people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
**Output:**
`[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

---

"""


@print_output
def queue_reconstruct_by_height(
    people: list[list[int]]
) -> list[list[int]]:
    if not people:
        return []
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for h, k in people:
        res.insert(k, [h, k])
    return res


"""

## 9) Validate Binary Search Tree

**Difficulty:** Medium

Given the root of a binary tree, 
determine if it is a valid binary search tree.

### Example

**Input:**
`root = [2,1,3]`
**Output:**
`true`

---
"""


@print_output
def validate_bst(root: TreeNode) -> bool:
    if root is None:
        return True
    st = [(root, float("-inf"), float("inf"))]
    while st:
        node, low, high = st.pop()
        if not (low < node.key < high):
            return False
        if node.left:
            st.append((node.left, low, node.key))
        if node.right:
            st.append((node.right, node.key, high))
    return True


"""

## 10) Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium

There are some spherical balloons represented as 
intervals `points`. Return the minimum number of 
arrows that must be shot to burst all balloons.

### Example

**Input:**
`points = [[10,16],[2,8],[1,6],[7,12]]`
**Output:**
`2`

---

"""

@print_output
def minimum_number_arrow(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    first_end = points[0][1]
    for i in range(1, len(points)):
        start, end = points[i][0], points[i][1]
        if start > first_end:
            arrows += 1
            first_end = end
    return arrows



if __name__ == "__main__":
    # path_exists_in_graph(
    #     n = 3, 
    #     edges = [[0,1],[1,2],[2,0]], 
    #     source = 0, 
    #     destination = 2
    # )
    # bt2 = create_bt([3,9,20,None,None,15,7])
    # level_order_traversal(bt2)
    # grid = [["1","1","0"],["1","1","0"],["0","0","1"]]
    # num_islands(grid)
    # can_pass_all_courses(numCourses = 2, prerequisites = [[1,0]])
    # queue_reconstruct_by_height([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    # jump_game([2,3,1,1,4])
    # minimum_number_arrow([[10,16],[2,8],[1,6],[7,12]])
    bt2 = create_bt([2,1,3])
    validate_bst(bt2)