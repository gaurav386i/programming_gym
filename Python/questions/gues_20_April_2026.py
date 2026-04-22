from collections import deque
from utils import print_return_value, print_linklist
from heapq import heappush, heappop

"""
---

## 1) Number of Recent Calls

**Topic:** Queue, Design
**Difficulty:** Easy

You have a `RecentCounter` class which counts the number of recent requests
within a certain time frame.

Implement the `RecentCounter` class:

* `RecentCounter()` Initializes the counter with zero recent requests.
* `ping(t)` Adds a new request at time `t`, where `t` is in milliseconds, and
returns the number of requests that have happened in the inclusive
range `[t - 3000, t]`.

Each call to `ping` uses a strictly larger value of `t` than the previous call.

### Example 1

**Input:**
`["RecentCounter","ping","ping","ping","ping"]`
`[[],[1],[100],[3001],[3002]]`

**Output:**
`[null,1,2,3,3]`

### Constraints

* `1 <= t <= 10^9`
* At most `10^4` calls will be made to `ping`

---
"""


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int):
        self.q.append(t)

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


"""

## 2) Middle of the Linked List

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Easy

Given the `head` of a singly linked list, return the middle node of the linked
list.

If there are two middle nodes, return the second middle node.

### Example 1

**Input:**
`head = [1,2,3,4,5]`
**Output:**
`[3,4,5]`

### Example 2

**Input:**
`head = [1,2,3,4,5,6]`
**Output:**
`[4,5,6]`

### Constraints

* The number of nodes in the list is in the range `[1, 100]`
* `1 <= Node.val <= 100`

---
"""


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


@print_return_value
def middle_of_ll(head: Node) -> Node:
    if head is None:
        return head
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.val


head1 = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)

head1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

"""

## 3) Invert Binary Tree

**Topic:** Tree, Binary Tree
**Difficulty:** Easy

Given the `root` of a binary tree, invert the tree, and return its root.

### Example 1

**Input:**
`root = [4,2,7,1,3,6,9]`
**Output:**
`[4,7,2,9,6,3,1]`

### Example 2

**Input:**
`root = [2,1,3]`
**Output:**
`[2,3,1]`

### Constraints

* The number of nodes in the tree is in the range `[0, 100]`
* `-100 <= Node.val <= 100`

---

"""


class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


def invert_bt(root: TreeNode) -> TreeNode:
    if root is None:
        return root
    root.left, root.right = root.right, root.left

    invert_bt(root.left)
    invert_bt(root.right)

    return root


"""

## 4) Merge Sorted Array

**Topic:** Sorting, Two Pointers, Array
**Difficulty:** Easy

You are given two integer arrays `nums1` and `nums2`, sorted in
non-decreasing order,
and two integers `m` and `n`, representing the number of valid elements in
`nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should be stored inside `nums1`.

### Example 1

**Input:**
`nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
**Output:**
`[1,2,2,3,5,6]`

### Example 2

**Input:**
`nums1 = [1], m = 1, nums2 = [], n = 0`
**Output:**
`[1]`

### Constraints

* `nums1.length == m + n`
* `nums2.length == n`
* `0 <= m, n <= 200`

---
"""


@print_return_value
def merge_two_sorted_arr_in_one(
    nums1: list[int], nums2: list[int], m: int, n: int
) -> list[int]:
    if not nums1 or not nums2:
        return nums1 if nums1 else nums2
    p1 = m - 1
    p2 = n - 1
    k = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[k] = nums1[p1]
            p1 -= 1
        else:
            nums1[k] = nums2[p2]
            p2 -= 1
        k -= 1
    while p2 > 0:
        nums1[k] = nums2[p2]
        p2 += 1
        k += 1
    return nums1


"""

## 5) Add Two Numbers

**Topic:** Linked List, Pointer Manipulation
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

### Constraints

* The number of nodes in each linked list is in the range `[1, 100]`
* `0 <= Node.val <= 9`

---
"""


@print_return_value
def add_val_from_two_ll(l1: Node, l2: Node) -> Node:
    dummy = Node(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = l1_val + l2_val + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


"""

## 6) Minimum Remove to Make Valid Parentheses

**Topic:** Stack, String
**Difficulty:** Medium

Given a string `s` of `'('`, `')'`, and lowercase English characters,
remove the minimum number of parentheses so that the resulting string is valid.

Return any valid string.

### Example 1

**Input:**
`s = "lee(t(c)o)de)"`
**Output:**
`"lee(t(c)o)de"`

### Example 2

**Input:**
`s = "a)b(c)d"`
**Output:**
`"ab(c)d"`

### Constraints

* `1 <= s.length <= 10^5`
* `s[i]` is either `'('`, `')'`, or a lowercase English letter

---
"""


@print_return_value
def return_valid_parentheses(word: str) -> str:
    if not word:
        return ""
    st = []
    remove = set()
    result = []
    for i, ch in enumerate(word):
        if ch == "(":
            st.append((i))
        elif ch == ")":
            if st:
                st.pop()
            else:
                remove.add(i)
    while st:
        remove.add(st.pop())

    for i, ch in enumerate(word):
        if i not in remove:
            result.append(ch)
    return "".join(result)


"""

## 7) Minimum Size Subarray Sum

**Topic:** Sliding Window, Array
**Difficulty:** Medium

Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a subarray whose sum is greater than or equal
to `target`. If there is no such subarray, return `0` instead.

### Example 1

**Input:**
`target = 7, nums = [2,3,1,2,4,3]`
**Output:**
`2`

### Example 2

**Input:**
`target = 11, nums = [1,1,1,1,1,1,1,1]`
**Output:**
`0`

### Constraints

* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^4`

---
"""


@print_return_value
def min_size_sub_arr_sum(nums: list[int], target: int) -> int:
    # target = 7, nums = [2,3,1,2,4,3]
    if not nums:
        return 0
    left = 0
    min_size = float("inf")
    curr_sum = 0
    for right in range(1, len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            curr_sum -= nums[left]
            min_size = min(min_size, right - left + 1)
            left += 1

    return 0 if curr_sum == float("inf") else min_size


"""

## 8) Reorganize String

**Topic:** Heap, Greedy, String
**Difficulty:** Medium

Given a string `s`, rearrange the characters of `s` so that any two
adjacent characters are not the same.

Return any possible rearrangement of `s` or return an empty string
if not possible.

### Example 1

**Input:**
`s = "aab"`
**Output:**
`"aba"`

### Example 2

**Input:**
`s = "aaab"`
**Output:**
`""`

### Constraints

* `1 <= s.length <= 500`
* `s` consists of lowercase English letters

---
"""


@print_return_value
def rearrange_ch(word: str) -> str:
    if not word:
        return ""
    max_heap = []
    freq = {}
    resp = []
    prev_count, prev_ch = 0, ""
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    for key, val in freq.items():
        heappush(max_heap, (-val, key))
    while max_heap:
        count, ch = heappop(max_heap)
        resp.append(ch)
        if prev_count < 0:
            heappush(max_heap, (prev_count, prev_ch))
        count += 1
        prev_count, prev_ch = count, ch
    arranged = "".join(resp)
    return arranged if len(arranged) == len(word) else ""


"""
## 9) Kth Smallest Element in a Sorted Matrix

**Topic:** Heap, K-way Merge
**Difficulty:** Medium

Given an `n x n` matrix where each of the rows and columns is sorted in
ascending order, return the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the
`k`th distinct element.

### Example 1

**Input:**
`matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`
**Output:**
`13`

### Example 2

**Input:**
`matrix = [[-5]], k = 1`
**Output:**
`-5`

### Constraints

* `n == matrix.length == matrix[i].length`
* `1 <= n <= 300`
* `1 <= k <= n * n`

---
"""


@print_return_value
def kth_smallest_elm_in_sorted_matrix(mat: list[list[int]], kth: int) -> int:
    # matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    if not mat:
        return 0
    min_heap = []
    resp = []
    for i, list in enumerate(mat):
        heappush(min_heap, (list[0], 0, i))
    count = 0
    resp
    while min_heap and count <= kth - 1:
        elm, e_idx, l_idx = heappop(min_heap)

        if l_idx < len(mat) and e_idx + 1 < len(mat[l_idx]):
            heappush(min_heap, (mat[l_idx][e_idx + 1], e_idx + 1, l_idx))
        count += 1
        if count == kth - 1:
            resp = elm
    return elm


"""

## 10) Boats to Save People

**Topic:** Sorting, Two Pointers, Greedy
**Difficulty:** Medium

You are given an array `people` where `people[i]` is the weight of
the `i`th person, and an infinite number of boats where each boat
can carry a maximum weight of `limit`.

Each boat carries at most two people at the same time, provided
the sum of their weights is at most `limit`.

Return the minimum number of boats to carry every given person.

### Example 1

**Input:**
`people = [1,2], limit = 3`
**Output:**
`1`

### Example 2

**Input:**
`people = [3,2,2,1], limit = 3`
**Output:**
`3`

### Constraints

* `1 <= people.length <= 5 * 10^4`
* `1 <= people[i] <= limit <= 3 * 10^4`

---
"""


@print_return_value
def boats_to_save_people(people: list[int], limit: int) -> int:
    if not people:
        return 0
    people.sort()
    start = 0
    end = len(people) - 1
    count = 0
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        count += 1
    return count


boats_to_save_people([3, 2, 2, 1], 3)

"""

## 11) Clone Graph

**Topic:** Graphs, DFS, BFS
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

### Constraints

* The number of nodes in the graph is in the range `[0, 100]`
* `1 <= Node.val <= 100`

---


"""


def deep_copy_of_graph_using_dfs(root: TreeNode) -> TreeNode:
    if root is None:
        return root
    old_to_new = {}
    def dfs(n)
    return result


"""

## 12) Binary Tree Level Order Traversal

**Topic:** Tree, Queue, BFS
**Difficulty:** Medium

Given the `root` of a binary tree, return the level order
traversal of its nodes’ values.

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

### Constraints

* The number of nodes in the tree is in the range `[0, 2000]`
* `-1000 <= Node.val <= 1000`

---
"""


@print_return_value
def bfs_level_order_traversal(root: TreeNode) -> None:
    # root = [3,9,20,null,null,15,7]
    if root is None:
        return
    q = deque()
    q.append(root)
    result = []
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
        result.append(level)
    return result


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

""""

## Difficulty split

### Easy

1. Number of Recent Calls
2. Middle of the Linked List
3. Invert Binary Tree
4. Merge Sorted Array

### Medium

5. Add Two Numbers
6. Minimum Remove to Make Valid Parentheses
7. Minimum Size Subarray Sum
8. Reorganize String
9. Kth Smallest Element in a Sorted Matrix
10. Boats to Save People
11. Clone Graph
12. Binary Tree Level Order Traversal

## Topic coverage check

* sorting → Merge Sorted Array, Boats to Save People
* stack → Minimum Remove to Make Valid Parentheses
* heap → Reorganize String, Kth Smallest Element in a Sorted Matrix
* two pointers → Merge Sorted Array, Boats to Save People
* slow and fast → Middle of the Linked List
* sliding window → Minimum Size Subarray Sum
* k-way merge → Kth Smallest Element in a Sorted Matrix
* linked list → Middle of the Linked List, Add Two Numbers
* queue → Number of Recent Calls, Binary Tree Level Order Traversal
* tree → Invert Binary Tree, Binary Tree Level Order Traversal
* graphs → Clone Graph
* greedy → Reorganize String, Boats to Save People

I can also make a third set, but biased toward interview patterns you
found hardest.


"""
