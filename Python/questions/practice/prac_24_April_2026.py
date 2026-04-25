from collections import deque
from typing import Optional, List, Any
from heapq import heappush, heappop

"""

---

## 1) Valid Parentheses

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

---
"""


def is_matching(a: str, b: str) -> bool:
    if a == "(" and b == ")":
        return True
    if a == "[" and b == "]":
        return True
    if a == "{" and b == "}":
        return True
    return False


def valid_parentheses(string: str) -> bool:
    if not string:
        return True
    st = []
    for ch in string:
        if ch in ("(", "[", "{"):
            st.append(ch)
        else:
            if st and is_matching(st[-1], ch) is False:
                return False
            else:
                st.pop()
    if st:
        return False
    return True


"""

## 2) Number of Recent Calls

**Difficulty:** Easy

You have a `RecentCounter` class which counts the number of recent 
requests within a certain time frame.

Implement the `RecentCounter` class:

* `RecentCounter()` Initializes the counter with zero recent requests.
* `ping(t)` Adds a new request at time `t`, where `t` is in milliseconds, 
and returns the number of requests that have happened in the inclusive range 
`[t - 3000, t]`.

Each call to `ping` uses a strictly larger value of `t` than the previous call.

### Example 1

**Input:**
`["RecentCounter","ping","ping","ping","ping"]`
`[[],[1],[100],[3001],[3002]]`

**Output:**
`[null,1,2,3,3]`

---
"""


class RecentCounter:
    def __init__(self):
        self.recent_requests = deque()

    def ping(self, t: int) -> list[int]:
        self.recent_requests.append(t)
        while self.recent_requests and self.recent_requests[0] < t - 3000:
            self.recent_requests.popleft()
        return len(self.recent_requests)


"""

## 3) Path Sum

**Difficulty:** Easy

Given the `root` of a binary tree and an integer `targetSum`, return `true` 
if the tree has a root-to-leaf path such that adding up all the values 
along the path equals `targetSum`.

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
"""


class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.right: TreeNode | None = None
        self.left: TreeNode | None = None


def create_bt(arr: List[Any]) -> Optional[TreeNode]:
    """
    Convert level-order list representation of a binary tree
    into an actual binary tree.

    Example:
    [10, 5, 15, 3, 7, None, 18]
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def bt_path_sum(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    if not root.left and not root.right:
        return target == root.key
    remaining = target - root.key
    return (
        bt_path_sum(root.left, remaining) or bt_path_sum(root.right, remaining)
    )


def bt_itr_path_sum(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    st = [(root, target - root.key)]
    while st:
        node, remianing = st.pop()
        if node.left is None and node.right is None:
            if remianing == 0:
                return True

        if node.right:
            st.append((node.right, remianing - node.right.key))
        if node.left:
            st.append((node.left, remianing - node.left.key))

    return False


"""

## 4) Sort Colors

**Difficulty:** Medium

Given an array `nums` with `n` objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent.

Use the integers `0`, `1`, and `2` to represent the colors red, 
white, and blue respectively.

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

---
"""


def sort_colors(colors: list[int]) -> list[int]:
    if not colors:
        return []
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
            colors[high], colors[min] = colors[mid], colors[high]
            mid += 1
            high -= 1
    return colors


"""
## 5) Minimum Remove to Make Valid Parentheses

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

---
"""


def remove_to_make_valid_parenthese(word: str) -> str:
    if not word:
        return ""
    st = []
    remove = set()
    for i, ch in enumerate(word):
        if ch == "(":
            st.append(i)
        elif ch == ")":
            if st:
                st.pop()
            else:
                remove.add(i)
    while st:
        remove.add(st.pop())
    result = []
    for i, ch in enumerate(word):
        if i not in remove:
            result.append(ch)

    return "".join(result)


"""

## 6) Minimum Size Subarray Sum

**Difficulty:** Medium

Given an array of positive integers `nums` and a positive integer 
`target`, return the minimal length of a subarray whose sum is greater 
than or equal to `target`. If there is no such subarray, return `0` instead.

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

---
"""


def minimum_sub_arr_sum(nums: list[int], target: int) -> int:
    if not nums:
        return 0
    left = 0
    total = 0
    best = float("inf")
    for right in range(len(nums)):
        total += nums[right]
        while total > target:
            total -= nums[left]
            left += 1
            best = min(best, right - left + 1)
    return best if total == target else 0


"""

## 7) Linked List Cycle II

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

---

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_ll(arr: List[int]) -> Optional[Node]:
    """
    Convert list representation into a linked list.

    Example:
    [1, 2, 3, 4]
    """
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    return head


def detect_cycle_in_ll(head: Node) -> Node:
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
    slow = fast
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.val


head1 = Node(0)
n1 = Node(1)
head1.next = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n3.next = n1


"""

## 8) Kth Largest Element in an Array

**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, 
return the `k`th largest element in the array.

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

---

"""


def kth_largest_element_insorted_order(
        nums: list[int], kth: int
) -> int | None:
    if len(nums) < kth:
        return None
    max_heap = []
    for num in nums:
        heappush(max_heap, -num)

    for _ in range(min(len(max_heap), kth - 1)):
        heappop(max_heap)

    return -heappop(max_heap)


"""

## 9) Search a 2D Matrix II

**Difficulty:** Medium

Write an efficient algorithm that searches for a value `target` 
in an `m x n` integer matrix.

This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

### Example 1

**Input:**
`matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 5`
**Output:**
`true`

### Example 2

**Input:**
`matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 20`
**Output:**
`false`

---

"""


def search_2d_matrix(mat: list[list[int]], target: int) -> bool:
    if not mat or not mat[0]:
        return False
    rows = len(mat)
    cols = len(mat[0])
    r = 0
    c = cols - 1

    while r < rows and c >= 0:
        if mat[r][c] == target:
            return True
        elif mat[r][c] < target:
            r += 1
        else:
            c -= 1

    return False




"""

## 10) Smallest Range Covering Elements from K Lists

**Difficulty:** Medium

You have `k` lists of sorted integers in non-decreasing order.

Find the smallest range that includes at least one number from 
each of the `k` lists.

If there are multiple answers, return the one with the smallest left endpoint.

### Example 1

**Input:**
`nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`
**Output:**
`[20,24]`

### Example 2

**Input:**
`nums = [[1,2,3],[1,2,3],[1,2,3]]`
**Output:**
`[1,1]`

---

"""


def smallest_range_covering_element_from_k_list(
        nums: list[list[int]]
) -> list[int]:
    if not nums or not nums[0]:
        return []
    heap = []
    max_value = float("-inf")
    for i, list in enumerate(nums):
        heappush(heap, (list[0], i, 0))
        max_value = max(max_value, list[0])
    best_range = [float("-inf"), float("inf")]
    while heap:
        min_val, l_idx, el_idx = heappop(heap)

        if max_value - min_val < best_range[1] - best_range[0]:
            best_range[0] = min_val
            best_range[1] = max_value
        if el_idx + 1 == len(nums[l_idx]):
            break
        next_val = nums[l_idx][el_idx + 1]
        heappush(heap, (next_val, l_idx, el_idx + 1))
        max_value = max(next_val, max_value)
    return best_range




"""

"""
