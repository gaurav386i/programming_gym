from heapq import heappush, heappop
from collections import deque

from prac_24_April_2026 import create_bt

"""

---

## 1) Contains Duplicate

**Difficulty:** Easy

Given an integer array `nums`, return `true` if any value appears at least 
twice in the array, and return `false` if every element is distinct.

### Example 1

**Input:**
`nums = [1,2,3,1]`
**Output:**
`true`

### Example 2

**Input:**
`nums = [1,2,3,4]`
**Output:**
`false`

---
"""


def is_contain_duplicate(nums: list[int]) -> bool:
    if not nums:
        return False
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] == nums[end]:
            return True
        else:
            start += 1
            end -= 1
    return False



"""

## 2) Balanced Binary Tree

**Difficulty:** Easy

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the 
depth of the two subtrees of every node never differs by more than one.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`true`

### Example 2

**Input:**
`root = [1,2,2,3,3,null,null,4,4]`
**Output:**
`false`

---
"""


class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def height_balanced_bt(root: TreeNode | None) -> bool:
    if root is None:
        return True
    
    def get_height(node: TreeNode | None) -> int:
        if node is None:
            return 0
        l_height = get_height(node.left)
        if l_height == -1:
            return -1
        r_height = get_height(node.right)
        if r_height == -1:
            return -1
        if abs(l_height - r_height) > 1:
            return -1
        return max(l_height, r_height) + 1
    
    return get_height(root) != -1


root1 = create_bt([3,9,20,None,None,15,7])

    
"""

## 3) Implement Queue using Stacks

**Difficulty:** Easy

Implement a first in first out (FIFO) queue using only two stacks.

Implement the `MyQueue` class:

* `push(x)`
* `pop()`
* `peek()`
* `empty()`

### Example 1

**Input:**
`["MyQueue","push","push","peek","pop","empty"]`
`[[],[1],[2],[],[],[]]`

**Output:**
`[null,null,null,1,1,false]`

---
"""


class MyQueue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x: int) -> None:
        self.in_stk.append(x)
    
    def _move(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
    
    def pop(self):
        self._move()
        return self.out_stk.pop()
    
    def peek(self):
        self._move()
        return self.out_stk[-1]
    
    def is_empty(self):
        return not self.in_stk and not self.out_stk


"""

## 4) Remove Nth Node From End of List

**Difficulty:** Medium

Given the head of a linked list, remove the `n`th node from the 
end of the list and return its head.

### Example 1

**Input:**
`head = [1,2,3,4,5], n = 2`
**Output:**
`[1,2,3,5]`

### Example 2

**Input:**
`head = [1], n = 1`
**Output:**
`[]`

---
"""


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None


def remove_nth_node_from_ll(head: ListNode, nth: int) -> ListNode | None:
    if head is None:
        return None
    dummy = TreeNode(0)
    dummy.next = head
    
    slow = dummy
    fast = dummy
    
    for _ in range(nth + 1):
        if fast is None:
            return head
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next

    return dummy.next

"""

## 5) Permutation in String

**Difficulty:** Medium

Given two strings `s1` and `s2`, return `true` if `s2` 
contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s 
permutations is the substring of `s2`.

### Example 1

**Input:**
`s1 = "ab", s2 = "eidbaooo"`
**Output:**
`true`

### Example 2

**Input:**
`s1 = "ab", s2 = "eidboaoo"`
**Output:**
`false`

---
"""


def get_chs_freq(word: str) -> dict[str, int]:
    resp = {}
    for ch in word:
        resp[ch] = resp.get(ch, 0) + 1
    return resp


def permutation_in_string(s1: str, s2: str) -> bool:
    if not s2 or len(s2) < len(s1):
        return False
    s1_freq = get_chs_freq(s1)  # {a: 1, b: 1}
    left = 0
    for right in range(len(s1) - 1, len(s2)):
        if s1_freq == get_chs_freq(s2[left:right + 1]):
            return True
        left += 1
    return False



"""

## 6) Top K Frequent Elements

**Difficulty:** Medium

Given an integer array `nums` and an integer 
`k`, return the `k` most frequent elements.

You may return the answer in any order.

### Example 1

**Input:**
`nums = [1,1,1,2,2,3], k = 2`
**Output:**
`[1,2]`

### Example 2

**Input:**
`nums = [1], k = 1`
**Output:**
`[1]`

---
"""


def k_freq_element(nums: list[int], kth: int) -> list[int]:
    if not nums:
        return []
    freq = {}
    max_heap = []
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    for k, v in freq:
        heappush(max_heap, (-v, k))
    resp = []
    for _ in range(min(kth, len(max_heap))):
        _, k = heappop(max_heap)
        resp.append(k)
    return resp


"""

## 7) Binary Tree Level Order Traversal

**Difficulty:** Medium

Given the `root` of a binary tree, return the level 
order traversal of its nodes’ values.

That is, from left to right, level by level.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[9,20],[15,7]]`

### Example 2

**Input:**
`root = [1]`
**Output:**
`[[1]]`

---
"""


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
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        resp.append(level)

    return resp



    
"""

## 8) Insert Interval

**Difficulty:** Medium

You are given an array of non-overlapping intervals sorted by 
start time, and an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that the resulting 
intervals are still non-overlapping and sorted by start time.

Return the new list of intervals.

### Example 1

**Input:**
`intervals = [[1,3],[6,9]], newInterval = [2,5]`
**Output:**
`[[1,5],[6,9]]`

### Example 2

**Input:**
`intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]`
**Output:**
`[[1,2],[3,10],[12,16]]`

---
"""


def insert_interval(
        intervals: list[list[int]],
        new_interval: list[int]
) -> list[list[int]]:
    if not intervals:
        return new_interval
    resp = []

    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        resp.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    resp.append(new_interval)

    while i < n:
        resp.append(intervals[i])
        i += 1
    return resp


"""

## 9) Clone Graph

**Difficulty:** Medium

Given a reference of a node in a connected undirected graph, 
return a deep copy of the graph.

Each node in the graph contains a value and a list of its neighbors.

### Example 1

**Input:**
`adjList = [[2,4],[1,3],[2,4],[1,3]]`
**Output:**
`[[2,4],[1,3],[2,4],[1,3]]`

### Example 2

**Input:**
`adjList = [[]]`
**Output:**
`[[]]`

---
"""


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list["GraphNode"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    old_to_new = {}
    
    def dfs(curr: GraphNode) -> GraphNode:
        if curr in old_to_new:
            return old_to_new[curr]
        
        clone = GraphNode(curr.val)
        old_to_new[curr] = clone
        for nei in curr.neighbors:
            clone.neighbors.append(dfs(nei))
        return clone
    if node is None:
        return None
    return dfs(node)
    



                              
"""

## 10) Car Fleet

**Difficulty:** Medium

There are `n` cars going to the same destination along a 
one-lane road. The destination is `target` miles away.

You are given two integer arrays `position` and `speed`, 
both of length `n`, where `position[i]` is the position 
of the `i`th car and `speed[i]` is the speed of the `i`th car.

A car can never pass another car ahead of it, but it can 
catch up to it and drive bumper to bumper at the same speed.

Return the number of car fleets that will arrive at the destination.

### Example 1

**Input:**
`target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`
**Output:**
`3`

### Example 2

**Input:**
`target = 10, position = [3], speed = [3]`
**Output:**
`1`

---

"""
def number_of_fleet(position: list[int], speed: list[int], target: int) -> int:
    if not position or not speed or not target:
        return 0
    speed_n_pos = list(zip(position, speed))
    speed_n_pos.sort(reverse=True)
    fleet = 0
    max_time = 0
    for pos, sp in speed_n_pos:
        time = (target - pos) // sp
        if time > max_time:
            fleet += 1
            max_time = time
    return fleet

"""

"""