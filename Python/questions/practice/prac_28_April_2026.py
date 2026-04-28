from prac_24_April_2026 import create_bt, create_ll

"""

---

## 1) Invert Binary Tree

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

---
"""
class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def invert_bt(root: TreeNode) -> TreeNode:
    if root is None:
        return root
    st = [root]
    resp = []
    while st:
        node = st.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)
    
    return root


bt1 = create_bt([4,2,7,1,3,6,9])

invert_bt(bt1)
"""

## 2) Reverse Linked List II

**Difficulty:** Medium

Given the `head` of a singly linked list and two integers 
`left` and `right` where `left <= right`, reverse the nodes 
of the list from position `left` to position `right`, and 
return the modified list.

### Example 1

**Input:**
`head = [1,2,3,4,5], left = 2, right = 4`
**Output:**
`[1,4,3,2,5]`

### Example 2

**Input:**
`head = [5], left = 1, right = 1`
**Output:**
`[5]`

---
"""


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None


def reverse_ll(head: ListNode, left: int, right: int) -> ListNode | None:
    if head is None or left == right:
        return head
    dummy = ListNode(0)
    dummy.next = head
    before_left = dummy
    for _ in range(left - 1):
        before_left = before_left.next
    tail = before_left.next
    curr = before_left
    prev = None
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    tail.next = curr
    before_left.next = prev

    return dummy.next
    
    
"""

## 3) Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

Given an array of integers `nums` sorted in non-decreasing order, 
find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
`nums = [5,7,7,8,8,10], target = 8`
**Output:**
`[3,4]`

### Example 2

**Input:**
`nums = [5,7,7,8,8,10], target = 6`
**Output:**
`[-1,-1]`

---

"""
def first_and_last_pos_of_elm_sorted_arr(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]
    def find_first():
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1  # keep moving left to get first occurance 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    def find_last():
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                ans = mid
                left = mid + 1  # keep moving right to get last occurance
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    return [find_first(), find_last()]



"""

## 4) Task Scheduler

**Difficulty:** Medium

You are given an array of CPU tasks, each represented by a 
character from `A` to `Z`, and a cooling time `n`.

Each cycle or interval allows the completion of one task. 
Tasks can be completed in any order, but there must be at 
least `n` intervals between two same tasks.

Return the minimum number of intervals required to complete all tasks.

### Example 1

**Input:**
`tasks = ["A","A","A","B","B","B"], n = 2`
**Output:**
`8`

### Example 2

**Input:**
`tasks = ["A","C","A","B","D","B"], n = 1`
**Output:**
`6`

---

"""
def task_scheduler(tasks: list[str], n: int) -> int:
    # Think of the most frequent task as creating blocks.
    #
    # Example:
    # A A A, n = 2
    #
    # A _ _ A _ _ A
    #
    # There are max_freq - 1 blocks before the last A.
    # Each block has size n + 1.
    #
    # For A A A:
    # max_freq - 1 = 2
    # n + 1 = 3
    #
    # So:
    # A _ _ | A _ _ | A
    #
    # Base formula:
    # (max_freq - 1) * (n + 1)
    #
    # Then add the number of tasks that have max frequency.
    #
    freq = {}
    for ts in tasks:
        freq[ts] = freq.get(ts, 0) + 1
    max_freq = max(freq.values())
    max_freq_count = 0
    for val in freq.values():
        if val == max_freq:
            max_freq_count += 1
    # formula for calculating number of cycle required  
    min_cycle = (max_freq - 1) * (n + 1) + max_freq_count
    # but sometimes enough other task are there to fill the idle times
    return max(min_cycle, len(tasks))


"""

## 5) Boats to Save People

**Difficulty:** Medium

You are given an array `people` where `people[i]` is 
the weight of the `i`th person, and an infinite number 
of boats where each boat can carry a maximum weight of `limit`.

Each boat carries at most two people at the same time, 
provided the sum of their weights is at most `limit`.

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

"""
def saves_people(people: list[int], limit: int) -> int:
    if not people:
        return 0
    start = 0
    end = len(people) - 1
    count = 0
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        count += 1
    return count 


print(saves_people([3,2,2,1], 3))


"""

"""