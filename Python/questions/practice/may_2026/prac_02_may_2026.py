from collections import deque
from heapq import heappush, heappop

from Python.questions.practice.may_2026.utils import (
     print_output,
     TreeNode,
     create_bt,
     ListNode, 
     create_ll
)
"""
---

# Set 3

## 1) Contains Duplicate

**Difficulty:** Easy

Given an integer array `nums`, return `true` if any 
value appears at least twice in the array, and 
return `false` if every element is distinct.

### Example

**Input:**
`nums = [1,2,3,1]`
**Output:**
`true`

---
"""


@print_output
def contains_duplicates(nums: list[int]) -> bool:
    if not nums:
        return True
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] == nums[right]:
            return True
        left += 1
        right -= 1
    return False


# contains_duplicates([1,2,3,4])

"""

## 2) Invert Binary Tree

**Difficulty:** Easy

Given the root of a binary tree, invert the tree, 
and return its root.

### Example

**Input:**
`root = [4,2,7,1,3,6,9]`
**Output:**
`[4,7,2,9,6,3,1]`

---

"""


@print_output
def invert_bt(root: TreeNode) -> TreeNode:
    if not root:
        return root
    st = [root]
    while st:
            node = st.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
   
    return root


bt1 = create_bt([4,2,7,1,3,6,9])

# invert_bt(bt1)

"""

## 3) Middle of the Linked List

**Difficulty:** Easy

Given the head of a singly linked list, return the middle 
node of the linked list.

If there are two middle nodes, return the second middle node.

### Example

**Input:**
`head = [1,2,3,4,5,6]`
**Output:**
`[4,5,6]`

---
"""
def mid_ll(head: ListNode) -> ListNode:
    if not head:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
"""

## 4) Find All Duplicates in an Array

**Difficulty:** Medium

Given an integer array `nums` of length `n` where all the 
integers of `nums` are in the range `[1, n]` and each integer
appears once or twice, return an array of all the integers
that appears twice.

### Example

**Input:**
`nums = [4,3,2,7,8,2,3,1]`
**Output:**
`[2,3]`

---

"""


@print_output
def return_all_duplicates_from_arr(nums: list[int]) -> list[int]:
    if not nums:
        return []
    result = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1

        if nums[idx] > 0:
            nums[idx] = -nums[idx]
        else:
            result.append(abs(nums[i]))
    return result


# return_all_duplicates_from_arr([4,3,2,7,8,2,3,1])
"""

## 5) Course Schedule II

**Difficulty:** Medium

There are a total of `numCourses` courses you have to take,
labeled from `0` to `numCourses - 1`.

Return the ordering of courses you should take to finish all
courses. If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

### Example

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`[0,1]`

---
"""


@print_output
def course_schedule(numsCourses: int, prerequisites: list[list[int]]) -> int:
    if not numsCourses or not prerequisites:
        return []
    # create grapgh and indegress:
    graph = {i: [] for i in range(numsCourses)}
    indegree = [0] * numsCourses
    q = deque()
    order = []
    
    for course, preq in prerequisites:
        graph[preq].append(course)
        indegree[course] += 1
    for i in range(numsCourses):
        if indegree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        order.append(v)
        for nei in graph[v]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)


    return order if len(order) == numsCourses else []


# course_schedule(2, [[1,0]])

"""

## 6) Sort List

**Difficulty:** Medium

Given the head of a linked list, return the list after sorting
it in ascending order.

### Example

**Input:**
`head = [4,2,1,3]`
**Output:**
`[1,2,3,4]`

---
"""


def get_mid_of_ll(head: ListNode) -> ListNode:
    if not head:
        return head
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
       
    return prev, slow


def merge_lls(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next


def sort_ll_in_ascending_order(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    prev, mid = get_mid_of_ll(head)
    prev.next = None
    
    left = sort_ll_in_ascending_order(head)
    right = sort_ll_in_ascending_order(mid)
    
    return merge_lls(left, right)
    



"""

## 7) Koko Eating Bananas

**Difficulty:** Medium

Given an array `piles` where `piles[i]` represents the number of
bananas in the `i`th pile, and an integer `h`, return the minimum
integer `k` such that Koko can eat all bananas within `h` hours.

### Example

**Input:**
`piles = [3,6,7,11], h = 8`
**Output:**
`4`

---
"""


@print_output
def koko_eating_banana(piles: list[int], h: int) -> int:
    if not piles:
        return 0
    left = 0
    right = len(piles) - 1
    while left <= right:
        mid = (right + left) // 2
        # calculate totat hours needed at speed=mid
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid  # ceil(pile/mid)
        if hours <= h:
            right = mid  # mid works try smaller values
        else:
            left = mid + 1 # mid too small try larger values
    return left


# koko_eating_banana([3,6,7,11], 8)

"""

## 8) Binary Tree Right Side View

**Difficulty:** Medium

Given the root of a binary tree, imagine yourself standing on the 
right side of it.

Return the values of the nodes you can see ordered from top to bottom.

### Example

**Input:**
`root = [1,2,3,null,5,null,4]`
**Output:**
`[1,3,4]`

---
"""


@print_output
def bt_right_side_view(root: TreeNode) -> list[int]:
    if not root:
        return root
    q = deque([root])
    result = []
    while q:
        l_size = len(q)
        for i in range(l_size):
            node = q.popleft()
            if i == l_size - 1:
                result.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


bt2 = create_bt([1,2,3,None,5,None,4])
# bt_right_side_view(bt2)

"""

## 9) Reorganize String

**Difficulty:** Medium

Given a string `s`, rearrange the characters 
so that no two adjacent characters are the same.

Return any possible rearrangement or return an 
empty string if not 
possible.

### Example

**Input:**
`s = "aab"`
**Output:**
`"aba"`

---
"""

@print_output
def reorg_string(s: str) -> str:
    if not s:
        return ""
    result = []
    freq = {}
    prev_count, prev_ch = 0, ""
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    mx_heap = []
    for k, v in freq.items():
        heappush(mx_heap, (-v, k))
    
    while mx_heap:
        count, ch = heappop(mx_heap)
        result.append(ch)
        if prev_count < 0:
            heappush(mx_heap, (prev_count, prev_ch))
        count += 1
        prev_count, prev_ch = count, ch

    arranged = "".join(result)
        
    return arranged if len(arranged) == len(s) else ""


# reorg_string("aabbccc")
        
        
"""

## 10) K Closest Points to Origin

**Difficulty:** Medium

Given an array of points where `points[i] = [xi, yi]` and an 
integer `k`, return the `k` closest points to the origin.

### Example

**Input:**
`points = [[1,3],[-2,2]], k = 1`
**Output:**
`[[-2,2]]`

---

"""

@print_output
def k_closest_point_to_origin(points: list[list[int]], k: int) -> list[list[int]]:
    resp = []
    if not points:
        return resp
    min_heap = []
    for x, y in points:
        heappush(min_heap, ((x * x + y * y), (x, y)))
    for _ in range(min(k, len(min_heap))):
        _, point = heappop(min_heap)
        resp.append(point)
    return resp


k_closest_point_to_origin([[1,3],[-2,2]], 1)
