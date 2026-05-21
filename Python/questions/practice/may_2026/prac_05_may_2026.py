from collections import deque
from heapq import heappush, heappop


from utils import create_ll, print_output, print_linked_list, create_bt

"""
# Set 5

## 1) Reverse Linked List

**Difficulty:** Easy

Given the head of a singly linked list, reverse the list and return the new head.

### Example

**Input:**
`head = [1,2,3,4,5]`
**Output:**
`[5,4,3,2,1]`

---
"""
class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None


def reverse_linklist(head: ListNode) -> ListNode:
    if head is None:
        return head
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

ll1 = create_ll([1,2,3,4,5])
# r_ll1 = reverse_linklist(ll1)
# print_linked_list(r_ll1)


"""

## 2) Implement Queue using Linked List

**Difficulty:** Easy

Design a queue using a linked list. Implement:

* `enqueue(x)`
* `dequeue()`
* `front()`
* `isEmpty()`

### Example

**Input:**
Operations: `enqueue(10), enqueue(20), front(), dequeue(), isEmpty()`
**Output:**
`10, 10, false`

---
"""
class _Node:
    def __init__(self, key: int = 0):
        self.key = key
        self.next: _Node | None = None
        self.prev: _Node | None = None


class MyQueue:
    def __init__(self, size: int = 0):
        self.size = size
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enqueue(self, value):
        new_node = _Node(value)
        first = self.head.next
        new_node.next = first
        first.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        self.size += 1

    
    def dequeue(self):
        if self.is_empty():
            return -1
        old_node = self.tail.prev
        value = old_node.key
        prev_node = old_node.prev
        self.tail.prev = prev_node
        prev_node.next = self.tail

        self.size -= 1
        return value
    
    def front(self):
        if self.is_empty():
            return -1
        return self.tail.prev.val
    
    def is_empty(self):
        return self.size ==  0
    

"""

## 3) BST Search, Insert, and Inorder Traversal

**Difficulty:** Easy

Implement three operations for a binary search tree:

1. Search for a value
2. Insert a value
3. Return inorder traversal

### Example

**Input:**
Insert: `5,3,7,2,4`
Search: `4`
**Output:**
`true`, inorder = `[2,3,4,5,7]`

---
"""


class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode| None = None

def insert_bt(root: TreeNode | None, key: int) -> TreeNode:
    if root is None:
        return TreeNode(key)
    if root.key == key:
        return root
    elif root.key > key:
        root.left = insert_bt(root.left, key)
    else:
        root.right = insert_bt(root.right, key)
    return root

# 5,3,7,2,4
def insert_bt_itr(root: TreeNode | None, key: int) -> TreeNode:
    parent = None
    curr = root
    while curr != None:
        parent = curr
        if curr.key == key:
            return root
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right
    if parent == None:
        return TreeNode(key)
    elif parent.key > key:
        parent.left = TreeNode(key)
    elif parent.key < key:
        parent.right = TreeNode(key)
    return root

def search_bst(root: TreeNode, value: int) -> bool:
    if root is None:
        return False
    curr = root
    while curr:
        if curr.key == value:
            return True
        elif curr.key > value:
            curr = curr.left
        else:
            curr = curr.right
    return False


def lavel_order_traversal(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    q = deque([root])
    res = []
    while q:
        l_size = len(q)
        level = []
        for _ in range(l_size):
            node = q.popleft()
            level.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


    
        
"""

## 4) Remove Duplicates from Sorted Array II

**Difficulty:** Medium

Given an integer array `nums` sorted in non-decreasing 
order, remove duplicates in-place such that each unique 
element appears at most twice.

Return the new length.

### Example

**Input:**
`nums = [1,1,1,2,2,3]`
**Output:**
`5`

---
"""

@print_output
def remove_duplicate_in_place(nums: list[int]) -> int:
    if not nums:
        return 0
    left = 2
    for right in range(2, len(nums)):
        if nums[right] != nums[left - 2]:
            nums[left] = nums[right]
            left += 1
    return left


# remove_duplicate_in_place([1,1,1,2,2,3])

"""

## 5) Reverse Linked List in Pairs

**Difficulty:** Medium

Given the head of a linked list, swap every two 
adjacent nodes and return the head of the modified list.

### Example

**Input:**
`head = [1,2,3,4]`
**Output:**
`[2,1,4,3]`

---

"""
def reverse_ll_in_pairs(head: ListNode) -> ListNode:
    if head is None:
        return head
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
    dummy = ListNode(0)
    dummy.next = head
    grp_prev = dummy

    while count >= 2:
        curr = grp_prev.next
        grp_curr = curr
        prev = None
        for _ in range(2):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tail = grp_curr
        tail.next = curr
        grp_prev.next = prev
        grp_prev = tail
        count -= 2
    return dummy.next

ll2 = create_ll([1,2,3,4])
rev_ll = reverse_ll_in_pairs(ll2)
# print_linked_list(rev_ll)

"""

## 6) Circular Queue Using Linked List

**Difficulty:** Medium

Implement a queue with fixed capacity `k` using a linked list. Support:

* `enqueue(x)`
* `dequeue()`
* `front()`
* `rear()`
* `isFull()`
* `isEmpty()`

### Example

**Input:**
Capacity `= 3`, operations: `enqueue(1), enqueue(2), enqueue(3), enqueue(4)`
**Output:**
`true, true, true, false`

---
"""


class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0

        self.head: ListNode | None = None
        self.tail: ListNode | None = None

        
    def enqueue(self, value):
        if self.is_full:
            return False
        if self.is_empty():
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.curr_capacity += 1
        return True
        
    
    def dequeue(self):
        if self.is_empty():
            return False
        removed_node = self.head.val
        self.head = self.head.next
        self.tail.next = self.head
        self.curr_capacity -= 1
        return removed_node
    
    def front(self):
        if self.is_empty():
            return None
        return self.head.val
    
    def rear(self):
        if self.is_empty():
            return None
        return self.tail.val

    def is_full(self):
        return self.capacity == self.curr_capacity
    
    def is_empty(self):
        return self.curr_capacity == 0


"""



## 7) Validate Binary Search Tree

**Difficulty:** Medium

Given the root of a binary tree, determine 
whether it is a valid binary search tree.

### Example

**Input:**
`root = [5,1,4,null,null,3,6]`
**Output:**
`false`

---
"""


def validate_bst(root: TreeNode) -> bool:
    def dfs(node, low: float, high: float):
        if node is None:
            return True
        if not low < node.key < high:
            return False
        else:
            return dfs(node.left, low, node.key) and dfs(node.right, node.key, high)
    return dfs(root, float("-inf", float("inf")))


def stk_validate_bst(root: TreeNode) -> bool:
    if root is None:
        return True
    st = [(root, float("-inf"), float("inf"))]
    while st:
        node, low, high = st.pop()
        if not (low < node.val < high):
            return False
        if node.left is not None:
            st.append((node.left, low, node.key))
        if node.right is not None:
            st.append((node.right, node.key, high))
    return True
        

"""

## 8) Daily Temperatures

**Difficulty:** Medium

Given an array of daily temperatures, return an array 
such that `answer[i]` is the number of days you have 
to wait after day `i` to get a warmer temperature.

### Example

**Input:**
`temperatures = [73,74,75,71,69,72,76,73]`
**Output:**
`[1,1,4,2,1,1,0,0]`

---
"""


@print_output
def daily_temperature(temperatures: list[int]) -> list[int]:
    if not temperatures:
        return []
    st = []

    resp = [0] * len(temperatures)
    for daily in range(len(temperatures)):
        while st and temperatures[daily] > temperatures[st[-1]]:
            prev_temp = st.pop()
            resp[prev_temp] = daily - prev_temp
        st.append(daily)
    return resp

# daily_temperature([73,74,75,71,69,72,76,73])

"""

## 9) Find K Pairs with Smallest Sums

**Difficulty:** Medium

You are given two sorted arrays `nums1` and `nums2` 
and an integer `k`.

Return the `k` pairs with the smallest sums.

### Example

**Input:**
`nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
**Output:**
`[[1,2],[1,4],[1,6]]`

---
"""

@print_output
def find_k_pairs_with_smallest_sums(
        nums1: list[int], nums2: list[int], k: int
) -> list[list[int]]:
    if not nums1 or not nums2:
        return []
    min_heap = []
    resp = []
    for i in range(min(k, len(nums1))):
        total = nums1[i] + nums2[0]
        heappush(min_heap, (total, i, 0))

    while min_heap:
        _, i, j = heappop(min_heap)
        resp.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            total = nums1[i] + nums2[j + 1]
            heappush(min_heap, (total, i, j + 1))
    
    return resp[:k] if len(resp) > k else resp

# find_k_pairs_with_smallest_sums([1,7,11], [2,4,6], 3)


"""

## 10) Add Two Numbers

**Difficulty:** Medium

You are given two non-empty linked lists representing 
two non-negative integers.

The digits are stored in reverse order, and each of 
their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

**Input:**
`l1 = [2,4,3], l2 = [5,6,4]`
**Output:**
`[7,0,8]`

---

"""

def add_two_ll_val(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    dummy = ListNode(0)
    carry = 0
    curr = dummy
    while l1 and l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        new_node = ListNode(total % 10)
        carry = total // 10
        curr.next = new_node
        curr = new_node
        l1 = l1.next
        l2 = l2.next
    return dummy.next

l1 = create_ll([2,4,3])
l2 = create_ll([5,6,4])

sum_ll = add_two_ll_val(l1, l2)

# print_linked_list(sum_ll)
        
