from collections import deque
import heapq
from utils import TreeNode, create_bt, print_output

"""
---

# NeetCode 150 - Practice Set 1

## 1) Binary Tree Maximum Path Sum
**Topic:** Tree
**Difficulty:** Hard

A **path** in a binary tree is a sequence of nodes where each pair of 
adjacent nodes in the sequence has an edge connecting them. A node can 
only appear in the sequence **at most once**. Note that the path does 
not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum path sum of any non-empty path*.

### Example
**Input:** `root = [-10,9,20,null,null,15,7]`
**Output:** `42`
**Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

requirements and assumptions:
how to handle if I/P is not provided or None .
input is a valid binary tree and with finite height and width 

Write approach again 
---

"""

def max_path_sum(root: TreeNode) -> int:
    if root is None:
        return 0
    max_path = float("-inf")

    def dfs(node: TreeNode) -> int:
        nonlocal max_path
        if node is None:
            return 0
        left_gain = max(0, dfs(node.left))
        right_gain = max(0, dfs(node.right))

        curr_gain = left_gain + node.key + right_gain
        max_path = max(max_path, curr_gain)

        return node.key + max(left_gain, right_gain)
    dfs(root)
    return max_path

    


"""

## 2) Cheapest Flights Within K Stops
**Topic:** Graph
**Difficulty:** Medium

There are `n` cities connected by some number of flights. You are given an 
array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that 
there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`, return *the cheapest 
price from `src` to `dst` with at most `k` stops*. If there is no such route, return `-1`.

### Example
**Input:** `n = 4, 
           flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
           src = 0, dst = 3, k = 1`
**Output:** `700`
**Explanation:** The path 0 -> 1 -> 3 costs 700.

requirements and assumptions :
how to handle if n or flights or k not given or None .
what if src == destination , do we need to check if price for a route is invalid 
assumptions :
n is valid int or 0 flights is valid list of edge/route, src and destinations are valid vertices
and k is valid int .

Core logic : start from src hop to neighbors and check if neighbor and keep calulating price and stop hop if
             hop > k and if found destination update destination min(cheapest_price, price )

---

"""


@print_output
def cheapest_flight_with_most_k_stops(
        n: int, 
        flights: list[list[int]],
        src: int, 
        dst: int, 
        k: int,
) -> int:
    if not n or not flights or src == dst:
        return 0
    
    graph = {i: [] for i in range(n)}
    visited = [False] * n
    visited[src] = True
    cheapest_price = float("inf")
    st = [src]

    for fromi, toi, pricei in flights:
        graph[fromi].append((toi, pricei))

    while st:
        node = st.pop()
        price = 0
        l = 0
        for nei, p in graph[node]:
            if visited[nei] == False and l <= k:
                
                visited[nei] = True
                l += 1
                price += p
                st.append(nei)
                if nei == dst:
                    cheapest_price = min(cheapest_price, price)
    return cheapest_price



    

"""

## 3) Merge Triplets to Form Target Triplet
**Topic:** Greedy
**Difficulty:** Medium

A **triplet** is an array of three integers. 
You are given a 2D integer array `triplets`, 
where `triplets[i] = [ai, bi, ci]` describes the `i-th` triplet. 
You are also given an integer array `target = [x, y, z]` that 
describes the target triplet you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` 
**any number of times** (possibly zero):
- Choose two indices `i` and `j` (`i != j`) and update 
`triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.

Return `true` if it is possible to obtain the `target` 
triplet `[x, y, z]` as an **element** of `triplets`, or `false` otherwise.

### Example
**Input:** `triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]`
**Output:** `true`

---
requirements and assumptions 
triples is an list of 3 int lists, target is list of 3 int 
triples can be None, 

Core logic :
naive : for each triplet in list iterate over all list and check if max of 
comparison will be equal
to target .
efficient : 





"""


@print_output
def merge_triplets(
        triplets: list[list[int]],
        target: list[int]
) -> int:
    if not triplets or not target:
        return False
    matched = set()

    for a, b, c in triplets:
        if a > target[0] or b > target[1] or c > target[2]:
            continue
        if a == target[0]:
            matched.add(0)
        if b == target[1]:
            matched.add(1)
        if c == target[2]:
            matched.add(2)
    
    return len(matched) == 3
    


"""

## 4) Time Based Key-Value Store
**Topic:** Binary Search
**Difficulty:** Medium

Design a time-based key-value data structure that can store 
multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the 
key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such 
that `set` was called previously, with `timestamp_prev <= timestamp`. 
If there are multiple such values, it returns the value associated with 
the largest `timestamp_prev`. If there are no values, it returns `""`.

### Example
**Input:** 
`["TimeMap", "set", "get", "get", "set", "get", "get"]`
`[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]`
**Output:**
`[null, null, "bar", "bar", null, "bar2", "bar2"]`

---




"""

class TimeMap:
    def __init__(self):
        self._store = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self._store:
            self._store[key] = []
        self._store[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ""
        values = self._store.get(key)
        result = ""
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (right + left) // 2
            v, tm = values[mid]
            if tm <= timestamp:
                result = v
                left = mid + 1
            else:
                right = mid - 1
        return result



"""

## 5) Evaluate Reverse Polish Notation
**Topic:** Stack
**Difficulty:** Medium

You are given an array of strings `tokens` that represents an arithmetic 
expression in a Reverse Polish Notation.

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:
- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse polish notation.

### Example
**Input:** `tokens = ["2","1","+","3","*"]`
**Output:** `9`
**Explanation:** ((2 + 1) * 3) = 9


requirements and assumptions:
what about empty tokens or no tokens 

---
"""

import operator

@print_output
def reverse_polish_notation(tokens: list[str]) -> int:
    if not tokens:
        return 0
    op_map = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b),
    }
    st = []
    
    for token in tokens:
        if token not in op_map:
            st.append(int(token))
        else:
            b = st.pop()
            a = st.pop()
            result = op_map[token](a, b)
            st.append(result)

    return st[-1]



if __name__ == "__main__":
    # 1) Binary Tree Maximum Path Sum
    # root = create_bt([-10,9,20,None,None,15,7])
    # max_path_sum(root)
    
    # 2) Cheapest Flights
    # cheapest_flight_with_most_k_stops(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
    
    # 3) Merge Triplets
    # merge_triplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5])
    
    # 4) Time Based Key-Value Store
    # obj = TimeMap()
    # obj.set("foo", "bar", 1)
    # print(obj.get("foo", 1))
    
    # 5) Evaluate RPN
    # reverse_polish_notation(["2","1","+","3","*"])
    pass
