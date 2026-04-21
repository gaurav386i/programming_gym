from collections import deque
from heapq import heappush, heappop

from utils import print_return_value

"""
* **4 Easy**
* **8 Medium**

This set covers:

* sorting
* stack
* heap
* two pointers
* slow and fast pointers
* sliding window
* k-way merge
* linked list
* queue
* tree
* graphs
* greedy

---

## 1) Valid Parentheses

**Topic:** Stack
**Difficulty:** Easy

Given a string `s` containing just the characters
`'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`,
determine if the input string is valid.

A string is valid if:

* open brackets are closed by the same type of brackets
* open brackets are closed in the correct order

### Example 1

**Input:**
`s = "()[]{}"`
**Output:**
`true`

### Example 2

**Input:**
`s = "(]"`
**Output:**
`false`

### Constraints

* `1 <= s.length <= 10^4`

---

"""


def is_matching(a: str, b: str) -> bool:
    if a == "(" and b == ")":
        return True
    elif a == "[" and b == "]":
        return True
    elif a == "{" and b == "}":
        return True
    else:
        return False


@print_return_value
def valid_parentheses(string: str) -> bool:
    if not string:
        return False
    st = []
    for ch in string:
        if ch in ("(", "{", "["):
            st.append(ch)
        else:
            if not st:
                return False
            elif is_matching(st[-1], ch) is False:
                return False
            else:
                st.pop()
    if st:
        return False
    else:
        return True


"""

## 2) Merge Two Sorted Lists

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

### Constraints

* The number of nodes in both lists is in the range `[0, 100]`

---
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merged_two_sorted_ll(l1: Node, l2: Node) -> Node:
    if l1 is None and l2 is None:
        return []
    dummy = Node(0)
    tail = dummy
    while l1 or l2:
        if l1.val < l2.val:
            # point to tail
            tail.next = l1
            # move l1 to next node
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

## 3) Maximum Depth of Binary Tree

**Topic:** Tree
**Difficulty:** Easy

Given the `root` of a binary tree, return its maximum depth.

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

### Constraints

* The number of nodes in the tree is in the range `[0, 10^4]`

---
"""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def max_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return max(
            max_bt(root.left),
            max_bt(root.right)
        ) + 1
# iterative BFS


@print_return_value
def bfs_max_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    q = deque([root])
    height = 0
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        height += 1
    return height


# iterative DFS


def dfs_max_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    stack = [(root, 1)]
    max_height = 0

    while stack:
        node, depth = stack.pop()
        max_height = max(depth, max_height)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    return max_height


"""

## 4) Implement Queue using Stacks

**Topic:** Queue, Stack, Design
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

### Constraints

* `1 <= x <= 10^9`

---
"""


class MyQueue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, val):
        self.in_stk.append(val)

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
        self._move()
        return not self.out_stk and not self.in_stk


"""

## 5) Sort Colors

**Topic:** Sorting, Two Pointers
**Difficulty:** Medium

Given an array `nums` with `n` objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent.

Use the integers `0`, `1`, and `2` to represent the colors red, white,
and blue.

You must solve this problem without using the library’s sort function.

### Example 1

**Input:**
`nums = [2,0,2,1,1,0]`
**Output:**
`[0,0,1,1,2,2]`

### Example 2

**Input:**
`nums = [2,0,1]`
**Output:**
`[0,1,2]`

### Constraints

* `1 <= nums.length <= 300`

---
"""


@print_return_value
def sort_colors(colors: list[int]) -> list[int]:
    if not colors:
        return colors
    low = 0
    mid = 0
    high = len(colors) - 1
    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            mid += 1
            low += 1
        elif colors[mid] == 1:
            mid += 1
        else:  # color[mid] == 2
            colors[high], colors[mid] = colors[mid], colors[high]
            mid += 1
            high -= 1
    return colors


"""

## 6) Linked List Cycle II

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium

Given the `head` of a linked list, return the node where the cycle begins.
If there is no cycle, return `null`.

Do not modify the linked list.

### Example 1

**Input:**
`head = [3,2,0,-4], pos = 1`
**Output:**
`tail connects to node index 1`

### Example 2

**Input:**
`head = [1,2], pos = 0`
**Output:**
`tail connects to node index 0`

### Constraints

* The number of nodes in the list is in the range `[0, 10^4]`

---
"""


@print_return_value
def detect_cycle_ll(head: Node) -> Node | None:
    if head is None:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


head = Node(0)
n1 = Node(1)
head.next = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n3.next = n1


"""

## 7) Longest Repeating Character Replacement

**Topic:** Sliding Window
**Difficulty:** Medium

You are given a string `s` and an integer `k`. You can choose any character of
the string and change it to any other uppercase English character
at most `k` times.

Return the length of the longest substring containing the same letter you can
get after performing at most `k` operations.

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

### Constraints

* `1 <= s.length <= 10^5`

---
"""


def longest_repeating_char_replacement(s: str, ops: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    best = 0
    for right in range(len(s)):
        ch = s[right]
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        while (right - left + 1) - max_freq > ops:
            count[s[left]] -= 1
            left += 1
        best = max(best, (right - left + 1))
    return best


"""

## 8) Kth Largest Element in an Array

**Topic:** Heap
**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, return the
`k`th largest element in the array.

Note that it is the `k`th largest element in sorted order,
not the `k`th distinct element.

### Example 1

**Input:**
`nums = [3,2,1,5,6,4], k = 2`
**Output:**
`5`

### Example 2

**Input:**
`nums = [3,2,3,1,2,4,5,5,6], k = 4`
**Output:**
`4`

### Constraints

* `1 <= k <= nums.length <= 10^5`

---
"""


@print_return_value
def kth_largest_element_in_arr(arr: list[int], kth: int) -> int:
    if not arr:
        return 0
    max_heap = []
    for i, num in enumerate(arr):
        heappush(max_heap, (-num, i))
    for _ in range(min(kth-1, len(max_heap))):
        heappop(max_heap)
    num, _ = heappop(max_heap)
    return -num


"""


## 9) Find K Pairs with Smallest Sums

**Topic:** K-way Merge, Heap
**Difficulty:** Medium

You are given two integer arrays `nums1` and `nums2` sorted in
ascending order and an integer `k`.

Define a pair `(u, v)` where one element is from the first array and the
other is from the second array.

Return the `k` pairs with the smallest sums.

### Example 1

**Input:**
`nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
**Output:**
`[[1,2],[1,4],[1,6]]`

### Example 2

**Input:**
`nums1 = [1,1,2], nums2 = [1,2,3], k = 2`
**Output:**
`[[1,1],[1,1]]`

### Constraints

* `1 <= nums1.length, nums2.length <= 10^5`
* `1 <= k <= 10^4`

---

## 10) Insert Interval

**Topic:** Greedy, Sorting, Intervals
**Difficulty:** Medium

You are given an array of non-overlapping intervals `intervals` sorted by
start time, and an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that the resulting intervals are
still non-overlapping and sorted by start time.

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

### Constraints

* `0 <= intervals.length <= 10^4`

---
"""


@print_return_value
def insert_intervals(
        intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    # core logic
    # add all intervals into result which comes before new_interval
    # merge all interval which overlaps which new interval
    # add updated new_interval
    # add remaining intervals
    if not intervals:
        return [new_interval]
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1
    return result


insert_intervals([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])

"""

## 11) Course Schedule

**Topic:** Graphs, Topological Sort
**Difficulty:** Medium

There are a total of `numCourses` courses you have to take,
labeled from `0` to `numCourses - 1`.

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

### Constraints

* `1 <= numCourses <= 2000`

---

"""


def can_finish_courses(
        numCourses: int,
        prerequisites: list[list[int]]
) -> bool:
    if not numCourses or not prerequisites:
        return False
    # prepare graph
    graph = {i: [] for i in range(len(numCourses))}
    indegree = [0] * numCourses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    q = deque()

    for i in range(len(numCourses)):
        if indegree[i] == 0:
            q.append(indegree[i])

    completed = 0

    while q:
        node = q.popleft()
        completed += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return completed == numCourses


"""

## 12) Container With Most Water

**Topic:** Two Pointers, Greedy
**Difficulty:** Medium

You are given an integer array `height` of length `n`. There are `n` vertical
lines drawn such that the two endpoints of the `i`th line are `(i, 0)`
and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds
the most water.

Return the maximum amount of water a container can store.

### Example 1

**Input:**
`height = [1,8,6,2,5,4,8,3,7]`
**Output:**
`49`

### Example 2

**Input:**
`height = [1,1]`
**Output:**
`1`

### Constraints

* `2 <= height.length <= 10^5`

---
"""


@print_return_value
def container_with_most_water(heights: list[int]) -> int:
    if not heights:
        return 0
    n = len(heights)
    start = 0
    end = n - 1
    max_capacity = 0
    while start < end:
        height = min(heights[start], heights[end])
        width = end - start
        capacity = height * width
        max_capacity = max(max_capacity, capacity)
        if heights[start] < heights[end]:
            start += 1
        else:
            end -= 1
    return max_capacity


"""

## Difficulty split

### Easy

1. Valid Parentheses
2. Merge Two Sorted Lists
3. Maximum Depth of Binary Tree
4. Implement Queue using Stacks

### Medium

5. Sort Colors
6. Linked List Cycle II
7. Longest Repeating Character Replacement
8. Kth Largest Element in an Array
9. Find K Pairs with Smallest Sums
10. Insert Interval
11. Course Schedule
12. Container With Most Water

## Topic coverage check

All requested topics are covered:

* sorting → Sort Colors, Insert Interval
* stack → Valid Parentheses, Queue using Stacks
* heap → Kth Largest Element
* two pointers → Container With Most Water, Sort Colors
* slow and fast → Linked List Cycle II
* sliding window → Longest Repeating Character Replacement
* k-way merge → Find K Pairs with Smallest Sums
* linked list → Merge Two Sorted Lists, Linked List Cycle II
* queue → Implement Queue using Stacks
* tree → Maximum Depth of Binary Tree
* graphs → Course Schedule
* greedy → Insert Interval, Container With Most Water


"""
