from heapq import heappush, heappop


"""

---

## 1) Move Zeroes

**Difficulty:** Easy

Given an integer array `nums`, move all `0`s to the end of it while
maintaining the relative order of the non-zero elements.

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


def move_zeroes(nums: list[int]) -> list[int]:
    if not nums or len(nums) < 2:
        return nums
    p1 = 0
    p2 = 1
    while p2 < len(nums):
        if nums[p2] > nums[p1]:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    return nums


"""

## 2) Maximum Depth of Binary Tree

**Difficulty:** Easy

Given the `root` of a binary tree, return its maximum depth.

A binary tree’s maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

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


class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def max_depth_of_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return max(max_depth_of_bt(root.left), max_depth_of_bt(root.right)) + 1


def itr_max_depth_of_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    q = [(root, 1)]
    max_depth = 0
    while q:
        node, depth = q.pop()
        max_depth = max(max_depth, depth)
        if node.right:
            q.append((node.right, depth + 1))
        if node.left:
            q.append((node.left, depth + 1))
    return max_depth


"""

## 3) Middle of the Linked List

**Difficulty:** Easy

Given the `head` of a singly linked list, return the
middle node of the linked list.

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

---
"""


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None


def find_mid_ll(head: ListNode) -> ListNode:
    if head is None:
        return head
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


"""

## 4) Longest Repeating Character Replacement

**Difficulty:** Medium

You are given a string `s` and an integer `k`. You can choose any character
of the string and change it to any other uppercase English character at
most `k` times.

Return the length of the longest substring containing the same letter you
can get after performing at most `k` operations.

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


def longest_repeating_char_replacement(s: str, k: int) -> int:
    char_freq = {}
    left = 0
    max_char = 0
    best = 0
    for right in range(len(s)):
        ch = s[right]
        char_freq[ch] = char_freq.get(ch, 0) + 1
        max_char = max(max_char, char_freq[ch])
        while (right - left + 1) - max_char > k:
            char_freq[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


"""

## 5) Reorder List

**Difficulty:** Medium

You are given the head of a singly linked-list. Reorder the list to be on
the following form:

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

You may not modify the values in the list’s nodes. Only nodes themselves
may be changed.

### Example 1

**Input:**
`head = [1,2,3,4]`
**Output:**
`[1,4,2,3]`

### Example 2

**Input:**
`head = [1,2,3,4,5]`
**Output:**
`[1,5,2,4,3]`

---

"""


def reorder_ll(head: ListNode) -> ListNode:
    if head is None:
        return head
    # core logic
    # find middle of linked list
    # split from middle , reverse second half of the ll
    # kind of merge both first and reveresed second half of ll
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow.next
    slow.next = None
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return head


"""

## 6) Search in Rotated Sorted Array

**Difficulty:** Medium

There is an integer array `nums` sorted in ascending order,
with distinct values.

Before being passed to your function, `nums` is possibly
rotated at an unknown pivot index.

Given the array `nums` after the possible rotation and an
integer `target`, return the index of `target` if it
is in `nums`, or `-1` if it is not in `nums`.

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


def search_rotated_sorted_arr(arr: list[int], target: int) -> int:
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        # go to the side which is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


"""

## 7) K Closest Points to Origin

**Difficulty:** Medium

Given an array of points where `points[i] = [xi, yi]`
represents a point on the X-Y plane and an integer `k`,
return the `k` closest points to the origin `(0, 0)`.

The distance between two points is the Euclidean distance.

You may return the answer in any order.

### Example 1

**Input:**
`points = [[1,3],[-2,2]], k = 1`
**Output:**
`[[-2,2]]`

### Example 2

**Input:**
`points = [[3,3],[5,-1],[-2,4]], k = 2`
**Output:**
`[[3,3],[-2,4]]`

---

"""


def k_closest_point_to_origin(
        points: list[list[int]], k: int
) -> list[list[int]]:
    if not points or len(points) < k:
        return []

    # we need to calculate euclidean distance
    min_heap = []
    resp = []

    for x, y in points:
        heappush(min_heap, ((x * x + y * y), x, y))

    for _ in range(min(len(min_heap), k)):
        _, x, y = heappop(min_heap)
        resp.append([x, y])
    return resp


"""

## 8) Non-overlapping Intervals

**Difficulty:** Medium

Given an array of intervals `intervals` where
`intervals[i] = [starti, endi]`, return the minimum number of
intervals you need to remove to make the rest of the intervals
non-overlapping.

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
"""


def count_non_overlapping_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    count = 0
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start < prev_end:
            count += 1
        else:
            prev_end = end
    return count


"""

## 9) Number of Provinces

**Difficulty:** Medium

There are `n` cities. Some of them are connected, while some are not.
If city `a` is connected directly with city `b`, and city `b` is
connected directly with city `c`, then city `a` is connected indirectly
with city `c`.

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

"""


def get_dfs(mat: list[list[int]], r: int, c: int) -> None:
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] == 0:
        return
    # mark visited
    mat[r][c] = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        get_dfs(mat, nr, nc)


def connected_province(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0
    rows = len(mat)
    cols = len(mat[0])

    connected = 0

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                connected += 1
                get_dfs(mat, r, c)
    return connected


print(connected_province([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

"""

## 10) Kth Smallest Element in a Sorted Matrix

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

---
"""


def kth_smallest_elem_from_sorted_mat(mat: list[list[int]], kth: int) -> int:
    if not mat or not mat[0]:
        return 0
    min_heap = []
    for i, list in enumerate(mat):
        heappush(min_heap, (list[0], i, 0))
    resp = []
    while min_heap:
        elm, l_idx, elm_idx = heappop(min_heap)
        resp.append(elm)
        if elm_idx + 1 < len(mat[l_idx]):
            heappush(min_heap, (mat[l_idx][elm_idx + 1], l_idx, elm_idx + 1))
    return resp[kth - 1] if len(resp) >= kth else resp[-1]


print(kth_smallest_elem_from_sorted_mat(
    [[1, 5, 9], [10, 11, 13], [12, 13, 15]],
    8)
)

"""


"""
