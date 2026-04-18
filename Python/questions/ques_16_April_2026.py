from utils import *
"""

---

## 1) Move Zeroes

**Topic:** Array, Two Pointers
**Difficulty:** Easy

Given an integer array `nums`, move all `0`s to the end of it while maintaining 
the relative order of the non-zero elements.

You must do this in-place.

### Example 1

**Input:**
`nums = [0,1,0,3,12]`
**Output:**
`[1,3,12,0,0]`

### Example 2

**Input:**
`nums = [0]`
**Output:**
`[0]`

---

"""

@print_return_value
def move_zeroes(nums: list[int]) -> list[int]:
    if not nums or len(nums) == 1:
        return nums
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums


"""
## 2) Valid Anagram

**Topic:** String, Hashing
**Difficulty:** Easy

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, 
and `false` otherwise.

### Example 1

**Input:**
`s = "anagram", t = "nagaram"`
**Output:**
`true`

### Example 2

**Input:**
`s = "rat", t = "car"`
**Output:**
`false`

---
"""
@print_return_value
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts or counts[ch] == 0:
            return False
        counts[ch] -= 1
    return True



"""

## 3) Merge Two Sorted Lists

**Topic:** Linked List
**Difficulty:** Easy

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list and return the head of the merged 
linked list.

### Example 1

**Input:**
`list1 = [1,2,4], list2 = [1,3,4]`
**Output:**
`[1,1,2,3,4,4]`

### Example 2

**Input:**
`list1 = [], list2 = []`
**Output:**
`[]`

---
"""
def merged_sorted_ll(l1: Node, l2: Node) -> Node:
    if l1 == None:
        return l2
    dummy = Node(0)
    tail = dummy
    while l1 < l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = 2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next

"""

## 4) Maximum Depth of Binary Tree

**Topic:** Tree, Binary Tree
**Difficulty:** Easy

Given the `root` of a binary tree, return its maximum depth.

A binary tree’s maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`3`

### Example 2

**Input:**
`root = [1,null,2]`
**Output:**
`2`

---

"""
def max_depth_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return max(max_depth_bt(root.left), max_depth_bt(root.right)) + 1


def iterative_max_depth_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth + 1))
    return max_depth

"""

## 5) Longest Repeating Character Replacement

**Topic:** Sliding Window
**Difficulty:** Medium

You are given a string `s` and an integer `k`. You can choose any 
character of the string and change it to any other uppercase English 
character at most `k` times.

Return the length of the longest substring containing the same letter 
you can get after performing at most `k` operations.

### Example 1

**Input:**
`s = "ABAB", k = 2`
**Output:**
`4`

### Example 2

**Input:**
`s = "AABABBA", k = 1`
**Output:**
`4`

---
"""
def character_replacement(s: str, k: int) -> int:
    #s = "ABAB", k = 2
    # you don't have to replace and check, just need to calculate if less freq
    # char count should be less that k
    count = {}
    left = 0
    max_freq = 0
    best = 0
    for right in range(len(s)):
        ch = s[right]
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        # check window validity 
        while (right - left + 1) - max_freq > k:
            # if window is not valid slice window
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)
    """
    left = 0, right = 0, count = {"A": 1}, max_freq = 1, best = 1
    left = 0, right = 1, count = {"A": 1, "B": 1}, max_freq = 1, best = 2
    left = 0, right = 2, count = {"A": 2, "B": 1}, max_freq = 2, best = 3
    left = 0, right = 3, count = {"A": 2, "B": 2}, max_freq = 2, best = 4
    """

    return best 

"""

## 6) Palindrome Linked List

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium

Given the `head` of a singly linked list, return `true` if it is a palindrome 
or `false` otherwise.

### Example 1

**Input:**
`head = [1,2,2,1]`
**Output:**
`true`

### Example 2

**Input:**
`head = [1,2]`
**Output:**
`false`

---
"""
def is_palindrome_ll(head: Node) -> bool:
    if head is None:
        return True
    slow = head
    fast = head
    # reach middle of ll
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # odd length list skip middle 
    if fast:
        slow = slow.next
    
    curr = slow.next
    prev =  None
    # reverse right half of ll
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    left = head
    right = prev
    # compare left and right of ll
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


"""

## 7) Top K Frequent Elements

**Topic:** Heap, Hashing
**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, return the `k` most 
frequent elements.

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
from heapq import heappush, heappop

def top_k_frequent_elm(nums: list[int], kth: int) -> list[int]:
    if not nums:
        return nums
    max_heap = []
    count = {}
    result = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key, val in count.items():
        heappush(max_heap, (-val, key))
    for _ in range(min(kth, len(max_heap))):
        _ , num = heappop(max_heap)
        result.append(num)
    return result
"""

## 8) Binary Tree Zigzag Level Order Traversal

**Topic:** Tree, BFS, Queue / Deque
**Difficulty:** Medium

Given the `root` of a binary tree, return the zigzag level order traversal 
of its nodes’ values.

That is, from left to right for the first level, then right to left for the 
next level, and alternate between them.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[20,9],[15,7]]`

### Example 2

**Input:**
`root = [1]`
**Output:**
`[[1]]`
---

"""

def bst_level_order_traversal_zigzag(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    result = []
    q = deque()
    q.append([root])
    left_to_right = True
    while q:
        q_size = len(q)
        level = deque()
        for _ in range(q_size):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result
        
    

"""

## 9) Rotting Oranges

**Topic:** Graphs, Matrices, BFS
**Difficulty:** Medium

You are given an `m x n` grid where each cell can have one of three values:

* `0` representing an empty cell
* `1` representing a fresh orange
* `2` representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten 
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a 
fresh orange. If this is impossible, return `-1`.

### Example 1

**Input:**
`grid = [[2,1,1],
         [1,1,0],
         [0,1,1]]`
**Output:**
`4`

### Example 2

**Input:**
`grid = [[2,1,1],
         [0,1,1],
         [1,0,1]]`
**Output:**
`-1`

---
"""
from collections import deque


def rotten_oranges(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid)
    minutes = 0
    fresh = 0
    q = deque()
    # collect all rotten oranges and count all free ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            if grid[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            # mark all oranges rotten in vicinity of rotten orange
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if(
                    0 <= nr < rows 
                    and 0 <= nc < cols
                    and grid[nr][nc] == 1
                ):
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
        # once one level is processed in BFS increment minutes by one
        minutes += 1
    
    return minutes if fresh == 0 else -1 
"""

## 10) Search in Rotated Sorted Array

**Topic:** Binary Search
**Difficulty:** Medium

There is an integer array `nums` sorted in ascending order, with distinct values.

Before being passed to your function, `nums` is possibly rotated at an unknown 
pivot index.

Given the array `nums` after the possible rotation and an integer `target`, 
return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
`nums = [4,5,6,7,0,1,2], target = 0`
**Output:**
`4`

### Example 2

**Input:**
`nums = [4,5,6,7,0,1,2], target = 3`
**Output:**
`-1`

---
"""
@print_return_value
def return_target_idx_in_sorted_rotated_array(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # left side is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0

return_target_idx_in_sorted_rotated_array(nums, target)

"""

## Difficulty split

### Easy

1. Move Zeroes
2. Valid Anagram
3. Merge Two Sorted Lists
4. Maximum Depth of Binary Tree

### Medium

5. Longest Repeating Character Replacement
6. Palindrome Linked List
7. Top K Frequent Elements
8. Binary Tree Zigzag Level Order Traversal
9. Rotting Oranges
10. Search in Rotated Sorted Array


"""
