from collections import deque
from prac_24_April_2026 import create_bt, create_ll

"""


---

## 1) Valid Anagram

**Difficulty:** Easy

Given two strings `s` and `t`, return `true` if `t` is an 
anagram of `s`, and `false` otherwise.

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
""""""
"""


def is_anagram(s: str, t: str) -> bool:
    if not s or len(s) < len(t):
        return False
    s_freq = {}
    t_freq = {}
    for ch in s:
        s_freq[ch] = s_freq.get(ch, 0) + 1
    for ch in t:
        t_freq[ch] = t_freq.get(ch, 0) + 1
    return s_freq == t_freq


"""

## 2) Merge Two Sorted Lists

**Difficulty:** Easy

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list and return the head of the 

merged linked list.

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


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linklist(ll: ListNode) -> None:
    res = []
    curr = ll
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print("->".join(res))


def merged_two_sorted_ll(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
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


"""

## 3) Search in a Binary Search Tree

**Difficulty:** Easy

You are given the `root` of a binary search tree and an integer `val`.

Find the node in the BST whose value equals `val` and return the subtree 
rooted with that node. If such a node does not exist, return `null`.

### Example 1

**Input:**
`root = [4,2,7,1,3], val = 2`
**Output:**
`[2,1,3]`

### Example 2

**Input:**
`root = [4,2,7,1,3], val = 5`
**Output:**
`[]`

---
"""


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def search_bst_return_val_sub_tree(root: TreeNode, value: int) -> TreeNode:
    if root is None:
        return root
    if root.key == value:
        return root
    if root.left and value < root.key:
        return search_bst_return_val_sub_tree(root.left, value)
    if root.right and value > root.key:
        return search_bst_return_val_sub_tree(root.right, value)


def itr_search_bst_return_val_sub_tree(
        root: TreeNode, value: int
) -> TreeNode:
    curr = root
    while curr:
        if curr.val == value:
            return curr
        elif curr.left and curr.val < value:
            curr = curr.left
        else:
            if curr.right:
                curr = curr.right
    return None


"""

## 4) Product of Array Except Self

**Difficulty:** Medium

Given an integer array `nums`, return an array `answer` such that `answer[i]` 
is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in `O(n)` time and without using 
division.

### Example 1

**Input:**
`nums = [1,2,3,4]`
**Output:**
`[24,12,8,6]`

### Example 2

**Input:**
`nums = [-1,1,0,-3,3]`
**Output:**
`[0,0,9,0,0]`

---
"""


def product_of_arr_except_self(nums: list[int]) -> list[int]:
    if not nums:
        return []
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1

    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


"""

## 5) Add Two Numbers

**Difficulty:** Medium

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example 1

**Input:**
`l1 = [2,4,3], l2 = [5,6,4]`
**Output:**
`[7,0,8]`

### Example 2

**Input:**
`l1 = [0], l2 = [0]`
**Output:**
`[0]`

---

"""
def add_two_sorted_ll(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    tail = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        new_node = ListNode(total % 10)

        tail.next = new_node
        new_node = tail
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


l1 = create_ll([2,4,3])

l2 = create_ll([5,6,4])


"""   

## 6) Group Anagrams

**Difficulty:** Medium

Given an array of strings `strs`, 
group the anagrams together. 
You can return the answer in any order.

### Example 1

**Input:**
`strs = ["eat","tea","tan","ate","nat","bat"]`
**Output:**
`[["bat"],["nat","tan"],["ate","eat","tea"]]`

### Example 2

**Input:**
`strs = [""]`
**Output:**
`[[""]]`

---
"""


def group_anagrams(strs: list[str]) -> list[list[int]]:
    if not strs:
        return []
    anagrm_map = {}
    for w in strs:
        s = "".join(sorted(w))
        if s in anagrm_map:
            anagrm_map[s].append(w)
        else:
            anagrm_map[s] = [w]
    return list(anagrm_map.values())


"""

## 7) Find Minimum in Rotated Sorted Array

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


def get_min_rotated_sorted_arr(nums: list[int]) -> int:
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

"""

"""

## 8) Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

Given the `root` of a binary tree, return the zigzag level order 
traversal of its nodes’ values.

That is, from left to right for the first level, then right to 
left for the next level, and alternate between them.

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


def bt_zigzag_level(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    q = deque([root])
    result = []
    left_to_right = True
    while q:
        level_size = len(q)
        level = deque()
        for _ in range(level_size):
            node = q.popleft()
            if left_to_right:
                level.append(node.key)
            else:
                level.appendleft(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
        left_to_right = not left_to_right
    return result


"""

## 9) Rotting Oranges

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
`grid = [[2,1,1],[1,1,0],[0,1,1]]`
**Output:**
`4`

### Example 2

**Input:**
`grid = [[2,1,1],[0,1,1],[1,0,1]]`
**Output:**
`-1`

---

"""


def rotten_oranges(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return -1
    rows = len(mat)
    cols = len(mat[0])
    q = deque()
    fresh = 0
    total = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 2:
                q.append((r, c))
            elif mat[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return -1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q and fresh > 0:
        l_size = len(q)
        for _ in range(l_size):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        total += 1
    return total if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

print(rotten_oranges(grid))

"""

## 10) Course Schedule

**Difficulty:** Medium

There are a total of `numCourses` courses you have to take, labeled from `0` 
to `numCourses - 1`.

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` 
indicates that you must take course `b` first if you want to take course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example 1

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`true`

### Example 2

**Input:**
`numCourses = 2, prerequisites = [[1,0],[0,1]]`
**Output:**
`false`

---
"""


def can_pass_courses(numCourse: int, prerequisites: list[list[int]]) -> bool:
    if not numCourse or not prerequisites:
        return False
    # prepare graph
    graph = {i: [] for i in range(numCourse)}
    indegrees = [0] * numCourse
    q = deque()
    # fill the graph:
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegrees[course] += 1
    for i in range(numCourse):
        if indegrees[i] == 0:
            q.append(course)
    completed = 0
    while q:
        node = q.popleft()
        completed += 1
        for nei in graph[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    
    return completed == numCourse

"""


"""
