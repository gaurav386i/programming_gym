from utils import *

"""
These are chosen to keep improving your weaker areas:

* binary search decisions
* tree recursion / traversal
* graph ordering
* interval case handling
* in-place array logic
* design intuition
* sorting-based thinking

---

## 1) Relative Sort Array

**Topic:** Array, Hashing, Sort
**Difficulty:** Easy

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, 
and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that:

* the relative ordering of items in `arr1` are the same as in `arr2`
* elements not in `arr2` are placed at the end in ascending order

### Example 1

**Input:**
`arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]`
**Output:**
`[2,2,2,1,4,3,3,9,6,7,19]`

---

## 2) Path Sum

**Topic:** Tree, DFS
**Difficulty:** Easy

Given the `root` of a binary tree and an integer `targetSum`, return `true` 
if the tree has a root-to-leaf path such that adding up all the values along 
the path equals `targetSum`.

### Example 1

**Input:**
`root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
**Output:**
`true`

### Example 2

**Input:**
`root = [1,2,3], targetSum = 5`
**Output:**
`false`

---

## 3) Sort List

**Topic:** Linked List, Sort, Merge Sort
**Difficulty:** Medium

Given the head of a linked list, return the list after sorting it in 
ascending order.

### Example 1

**Input:**
`head = [4,2,1,3]`
**Output:**
`[1,2,3,4]`

### Example 2

**Input:**
`head = [-1,5,3,4,0]`
**Output:**
`[-1,0,3,4,5]`

### Why this helps you

This strengthens both **linked lists** and **sorting as a pattern**,
especially merge sort on lists.

---

## 4) Find Minimum in Rotated Sorted Array

**Topic:** Binary Search
**Difficulty:** Medium

Suppose an array of length `n` sorted in ascending order is rotated 
between `1` and `n` times. Given the sorted rotated array `nums` of 
unique elements, return the minimum element.

You must write an algorithm that runs in `O(log n)` time.

### Example 1

**Input:**
`nums = [3,4,5,1,2]`
**Output:**
`1`

### Example 2

**Input:**
`nums = [4,5,6,7,0,1,2]`
**Output:**
`0`

---

## 5) Non-overlapping Intervals

**Topic:** Intervals, Greedy, Sort
**Difficulty:** Medium

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, 
return the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.

### Example 1

**Input:**
`intervals = [[1,2],[2,3],[3,4],[1,3]]`
**Output:**
`1`

### Example 2

**Input:**
`intervals = [[1,2],[1,2],[1,2]]`
**Output:**
`2`

---

## 6) Koko Eating Bananas

**Topic:** Binary Search
**Difficulty:** Medium

Koko loves to eat bananas. There are `n` piles of bananas, and the `i`th pile 
has `piles[i]` bananas. The guards will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed `k`. Each hour, she chooses 
some pile and eats up to `k` bananas from that pile.

Return the minimum integer `k` such that she can eat all bananas within 
`h` hours.

### Example 1

**Input:**
`piles = [3,6,7,11], h = 8`
**Output:**
`4`

### Example 2

**Input:**
`piles = [30,11,23,4,20], h = 5`
**Output:**
`30`

---

## 7) Binary Tree Right Side View

**Topic:** Tree, BFS, DFS
**Difficulty:** Medium

Given the `root` of a binary tree, imagine yourself standing on the right 
side of it. Return the values of the nodes you can see ordered from top to 
bottom.

### Example 1

**Input:**
`root = [1,2,3,null,5,null,4]`
**Output:**
`[1,3,4]`

### Example 2

**Input:**
`root = [1,null,3]`
**Output:**
`[1,3]`

---

## 8) Car Fleet

**Topic:** Stack, Sort
**Difficulty:** Medium

There are `n` cars going to the same destination along a one-lane road. 
The destination is `target` miles away.

You are given two integer arrays `position` and `speed`, both of length `n`, 
where `position[i]` is the position of the `i`th car and `speed[i]` is the 
speed of the `i`th car.

A car can never pass another car ahead of it, but it can catch up to it and 
drive bumper to bumper at the same speed.

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

## 9) Number of Provinces

**Topic:** Graphs, DFS, BFS, Union Find
**Difficulty:** Medium

There are `n` cities. Some of them are connected, while some are not. 
If city `a` is connected directly with city `b`, and city `b` is connected 
directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` 
if the `i`th city and the `j`th city are directly connected, and `0` otherwise.

Return the total number of provinces.

### Example 1

**Input:**
`isConnected = [[1,1,0],[1,1,0],[0,0,1]]`
**Output:**
`2`

### Example 2

**Input:**
`isConnected = [[1,0,0],[0,1,0],[0,0,1]]`
**Output:**
`3`

---

## 10) Alien Dictionary

**Topic:** Graphs, Topological Sort
**Difficulty:** Hard

There is a new alien language that uses the English alphabet. However, 
the order of the letters is unknown.

You are given a list of strings `words` from the alien language’s dictionary, 
where the strings are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in 
lexicographically increasing order by the new language’s rules. 
If there is no solution, return `""`. If there are multiple solutions, 
return any of them.

### Example 1

**Input:**
`words = ["wrt","wrf","er","ett","rftt"]`
**Output:**
`"wertf"`

### Example 2

**Input:**
`words = ["z","x","z"]`
**Output:**
`""`

---

# Best order for you to solve

To target your weak points well, do them in this order:

1. Path Sum
2. Relative Sort Array
3. Find Minimum in Rotateld Sorted Array
4. Binary Tree Right Side View
5. Non-overlapping Interval;,sD:Sls
6. Sort List
7. Koko Eating Bananas
8. Number of Provinces
9. Car Fleet
10. Alien Dictionary

# Why this set is good for you

* **Sort included:** Relative Sort Array, Sort List, Non-overlapping Intervals, 
Car Fleet
* **Tree recursion:** Path Sum, Binary Tree Right Side View
* **Binary search clarity:** Find Minimum, Koko
* **Graphs:** Number of Provinces, Alien Dictionary
* **Pattern recognition:** intervals, topological sort, linked list merge sort

"""
# +++++++++++++++++ #

"""
## 1) Relative Sort Array

**Topic:** Array, Hashing, Sort
**Difficulty:** Easy

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, 
and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that:

* the relative ordering of items in `arr1` are the same as in `arr2`
* elements not in `arr2` are placed at the end in ascending order

### Example 1

**Input:**
`arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]`
**Output:**
`[2,2,2,1,4,3,3,9,6,7,19]`

---
"""
def relative_arr_sort(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    count = {}
    result = []
    # count elem in arr1
    for num in arr1:
        count[num] = count.get(num, 0) + 1
    # add element to result in order of arr2
    for num in arr2:
        result.extend([num] * count[num])
        # remove it s only leftover numbers remain
        del count[num]
    # sort remain in ascending order
    remaining = sorted(count.keys())
    for num in remaining:
        result.extend([num] * remaining[num])


"""
## 2) Path Sum

**Topic:** Tree, DFS
**Difficulty:** Easy

Given the `root` of a binary tree and an integer `targetSum`, return `true` 
if the tree has a root-to-leaf path such that adding up all the values along 
the path equals `targetSum`.

### Example 1

**Input:**
`root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
**Output:**
`true`

### Example 2

**Input:**
`root = [1,2,3], targetSum = 5`
**Output:**
`false`

"""

def bfs_target_sum(root: TreeNode, target_sum: int) -> bool:
    if not root:
        return False
    
    # If this is a leafnode check if sum matches
    if not root.left and not root.right:
        return root.key == target_sum
    # Check remianing subtree with remaining sum
    remaining = target_sum - root.key

    return bfs_target_sum(root.left, remaining) or bfs_target_sum(root.right, remaining)


"""
## 3) Sort List

**Topic:** Linked List, Sort, Merge Sort
**Difficulty:** Medium

Given the head of a linked list, return the list after sorting it in 
ascending order.

### Example 1

**Input:**
`head = [4,2,1,3]`
**Output:**
`[1,2,3,4]`

### Example 2

**Input:**
`head = [-1,5,3,4,0]`
**Output:**
`[-1,0,3,4,5]`

"""
def get_ll_mid(head: None) -> Node:
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_ll(l1: Node, l2: Node) -> Node:
    dummy = Node(0)
    tail = dummy
    while l1 > l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next

def sort_ll_in_ascending(head: Node) -> Node:
    # get mid of linked list 
    mid = get_ll_mid(head)
    # break ll into two halfs
    right_head = mid.next
    mid.next = None
    left = sort_ll_in_ascending(head)
    right = sort_ll_in_ascending(right_head)
    return merge_ll(left, right)

"""
## 4) Find Minimum in Rotated Sorted Array

**Topic:** Binary Search
**Difficulty:** Medium

Suppose an array of length `n` sorted in ascending order is rotated 
between `1` and `n` times. Given the sorted rotated array `nums` of 
unique elements, return the minimum element.

You must write an algorithm that runs in `O(log n)` time.

### Example 1

**Input:**
`nums = [3,4,5,1,2]`
**Output:**
`1`

### Example 2

**Input:**
`nums = [4,5,6,7,0,1,2]`
**Output:**
`0`

---
"""
def min_rotated_sort_arr(nums: list[int]) -> int:
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


"""
## 5) Non-overlapping Intervals

**Topic:** Intervals, Greedy, Sort
**Difficulty:** Medium

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, 
return the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.

### Example 1

**Input:**
`intervals = [[1,2],[2,3],[3,4],[1,3]]`
**Output:**
`1`

### Example 2

**Input:**
`intervals = [[1,2],[1,2],[1,2]]`
**Output:**
`2`
"""

@print_return_value
def num_of_non_overlapping_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    prev_end = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start < prev_end:
            count += 1
        else:
            prev_end = end
    return count

"""
## 6) Koko Eating Bananas

**Topic:** Binary Search
**Difficulty:** Medium

Koko loves to eat bananas. There are `n` piles of bananas, and the `i`th pile 
has `piles[i]` bananas. The guards will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed `k`. Each hour, she chooses 
some pile and eats up to `k` bananas from that pile.

Return the minimum integer `k` such that she can eat all bananas within 
`h` hours.

### Example 1

**Input:**
`piles = [3,6,7,11], h = 8`
**Output:**
`4`

### Example 2

**Input:**
`piles = [30,11,23,4,20], h = 5`
**Output:**
`30`
"""
def koko_banana_eating_speed(piles: list[int], h: int) -> int:
    if not piles:
        return 0
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        # calculate total hours needed at speed = mid
        hour = 0
        for pile in piles:
            hour += (pile + mid -1) // mid # same as ceil(pile/mid)
        if hour <= h:
            right = mid # mid works, try smaller speed
        else:
            left = mid + 1  # mid too slow
    return left



"""
## 9) Number of Provinces

**Topic:** Graphs, DFS, BFS, Union Find
**Difficulty:** Medium

There are `n` cities. Some of them are connected, while some are not. 
If city `a` is connected directly with city `b`, and city `b` is connected 
directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` 
if the `i`th city and the `j`th city are directly connected, and `0` otherwise.

Return the total number of provinces.

### Example 1

**Input:**
`isConnected = [[1,1,0],[1,1,0],[0,0,1]]`
**Output:**
`2`

### Example 2

**Input:**
`isConnected = [[1,0,0],[0,1,0],[0,0,1]]`
**Output:**
`3`
"""

def dfs(grid: list[list[int]], r: int, c: int) -> bool:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
        return 
    # mark visited by changing value to 0
    grid[r][c] = 0
    # with nearby cells 
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)

@print_return_value
def number_of_province(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # number of disconnected graphs are number of cities 
                result += 1
                dfs(grid, r, c)
    return result


"""
## 7) Binary Tree Right Side View

**Topic:** Tree, BFS, DFS
**Difficulty:** Medium

Given the `root` of a binary tree, imagine yourself standing on the right 
side of it. Return the values of the nodes you can see ordered from top to 
bottom.

### Example 1

**Input:**
`root = [1,2,3,null,5,null,4]`
**Output:**
`[1,3,4]`

### Example 2

**Input:**
`root = [1,null,3]`
**Output:**
`[1,3]`

---
"""
from collections import deque

@print_return_value
def right_side_view_bt(root: TreeNode) -> list[int | None]:
    if not root:
        return []
    q = deque
    result = []
    q.append(root)
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == (level_size - 1):
                result.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


def dfs(root: TreeNode, depth: int, result: list[int]) -> None:
    if not root:
        return 
    if depth == len(result):
        result.append(root.key)
    dfs(root.right, depth + 1, result)
    dfs(root.left, depth + 1, result)

    return result

def right_side_view_dfs(root: TreeNode) -> list[int | None]:
    result = []
    dfs(root, 0, result)
    return result



"""
## 8) Car Fleet

**Topic:** Stack, Sort
**Difficulty:** Medium

There are `n` cars going to the same destination along a one-lane road. 
The destination is `target` miles away.

You are given two integer arrays `position` and `speed`, both of length `n`, 
where `position[i]` is the position of the `i`th car and `speed[i]` is the 
speed of the `i`th car.

A car can never pass another car ahead of it, but it can catch up to it and 
drive bumper to bumper at the same speed.

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

def car_fleet(target: int, positions: list[int], speeds: list[int]) -> int:
    cars = list(zip(positions, speeds))
    cars.sort(reverse=True)
    fleets = 0
    max_time = 0
    for pos, spd in cars:
        time = (target - pos) / spd
        if time > max_time:
            fleet += 1
            max_time = time
    return fleets


if __name__ == "__main__":
    pass