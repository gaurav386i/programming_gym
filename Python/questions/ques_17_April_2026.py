
from utils import print_return_value
"""
Here are **10 easy-to-medium practice questions** built around the topics you listed.

---

## 1) Reverse a Singly Linked List

**Topic:** Linked List, Pointer Manipulation
**Difficulty:** Easy

Given the head of a singly linked list, reverse the list and return the new head.

**Example**
Input: `1 -> 2 -> 3 -> 4 -> 5`
Output: `5 -> 4 -> 3 -> 2 -> 1`

**Follow-up:** Solve it both iteratively and recursively.

---
"""
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse_ll(head: Node) -> Node:
    if not head or head.next is None:
        return head
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

"""

## 2) Reverse Linked List Between Positions `left` and `right`

**Topic:** Linked List, Pointer Manipulation
**Difficulty:** Medium

Given the head of a singly linked list and two integers `left` and `right`, 
reverse the nodes from position `left` to position `right`, and return the 
modified list.

**Example**
Input: `1 -> 2 -> 3 -> 4 -> 5`, `left = 2`, `right = 4`
Output: `1 -> 4 -> 3 -> 2 -> 5`

**Focus:** Pointer reconnecting.

---
"""
def reverse_ll_between_two_points(head: Node, left: int, right: int) -> Node:
    if not head or right == left:
        return head
    dummy = Node(0)
    dummy.next = head
    group_prev = dummy
    prev = None
    for _ in range(left-1):
        group_prev = group_prev.next
    curr = group_prev.next
    tail = curr
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    group_prev.next = prev
    tail.next = curr
    
    return head
    
"""

## 3) Reverse Linked List in Pairs

**Topic:** Linked List, Pointer Manipulation
**Difficulty:** Medium

Given the head of a linked list, swap every two adjacent nodes and return 
the head of the modified list.

**Example**
Input: `1 -> 2 -> 3 -> 4`
Output: `2 -> 1 -> 4 -> 3`

**Follow-up:** Try both iterative and recursion-based versions.

---
"""
def reverse_ll_in_pairs(head: Node) -> Node:
    if not head or head.next is None:
        return head
    dummy = Node(0, head)
    group_prev = dummy
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
    while count >= 2:
          curr = group_prev.next
          group_curr = curr
          prev = None
          for _ in range(2):
              nxt = curr.next
              curr.next = prev
              prev = curr
              curr = nxt
          tail = group_curr
          tail.next = curr
          group_prev.next = prev
          group_prev = tail

          count -= 2
    return dummy.next

"""

## 4) Product of Array Except Self

**Topic:** Array Optimization
**Difficulty:** Medium

Given an integer array `nums`, return an array `answer` where `answer[i]` is 
equal to the product of all the elements of `nums` except `nums[i]`.

Do not use division.

**Example**
Input: `nums = [1,2,3,4]`
Output: `[24,12,8,6]`

**Focus:** Prefix and suffix products, time-space trade-off.

---

"""
@print_return_value
def prod_of_elm_except_self(nums: list[int]) -> list[int]:
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

## 5) Remove Duplicates From Sorted Array II

**Topic:** Array, Two Pointers, In-place Cleanup
**Difficulty:** Medium

Given a sorted integer array `nums`, remove duplicates in-place such that 
each unique value appears at most twice. Return the new length.

**Example**
Input: `nums = [1,1,1,2,2,3]`
Output length: `5`
Modified array prefix: `[1,1,2,2,3]`

**Focus:** Slow-fast pointer writing logic.

---
"""
@print_return_value
def remove_duplicates_from_sorted_arr(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    n = len(nums)
    slow = 2

    for fast in range(2, n):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

"""

## 6) Implement Queue Using a Linked List

**Topic:** Queue, Linked List
**Difficulty:** Easy

Design a queue using a linked list. Implement:

* `enqueue(x)`
* `dequeue()`
* `front()`
* `isEmpty()`

**Example**

* enqueue(10)
* enqueue(20)
* dequeue() → `10`
* front() → `20`

**Focus:** Using head and tail pointers correctly.

---
"""
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        removed_node = self.head.val
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return removed_node

    def front(self):
        if self.isEmpty():
            return None
        return self.head.val

    def isEmpty(self):
        return self.head is None
        

"""

## 7) Circular Queue Using Linked List

**Topic:** Queue, Linked List
**Difficulty:** Medium

Implement a queue with a fixed capacity `k` using a linked list. Support:

* `enqueue(x)`
* `dequeue()`
* `front()`
* `rear()`
* `isFull()`
* `isEmpty()`

**Example**
Capacity = `3`
enqueue(1), enqueue(2), enqueue(3), enqueue(4) → last insert should fail

**Focus:** Design + edge cases.

---
"""
class CircularQueue:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.current_capacity = 0
    
    
    def enqueue(self, val):
        if self.isFull():
            return None
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.current_capacity += 1
        return True
        
    def dequeue(self):
        if self.isEmpty():
            return None
        removed_node = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        
        self.current_capacity -= 1
        return removed_node

    def front(self):
        if self.isEmpty():
            return None
        return self.head.val

    def rear(self):
        if self.isEmpty():
            return None
        return self.tail.val

    def isFull(self):
        return self.current_capacity == self.capacity

    def isEmpty(self):
        return self.head is None

"""

## 8) BST Search, Insert, and Inorder Traversal

**Topic:** BST Basics
**Difficulty:** Easy

Implement three operations for a Binary Search Tree:

1. Search for a value
2. Insert a value
3. Return inorder traversal

**Example**
Insert: `5, 3, 7, 2, 4`
Search: `4` → `True`
Inorder output: `[2,3,4,5,7]`

**Focus:** BST property and recursion basics.

---
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_value_in_bt(root: TreeNode, target) -> bool:
    if root is None:
        return False
    if root.key == target:
        return True
    elif root.key > target:
        return search_value_in_bt(root.left. target)
    else:
        return search_value_in_bt(root.right, target)


def search_bst_iterative(root: TreeNode, target: int) -> bool:
    while root != None:
        if root.val == target:
            return True
        elif root.val < target:
            root = root.right
        else:
            root = root.left
    return False

def insert_in_bst(root: TreeNode, value: int) -> bool:
    if root is None:
       return TreeNode(value)
    elif root.key == value:
        return root
    elif root.key > value:
        root.left = insert_in_bst(root.left, value)
    else:
        root.right = insert_in_bst(root.right, value)
    return root

def iterative_bst_insert(root: TreeNode, value: int) -> bool:
    parent = None
    curr = root
    while curr != None:
        parent = curr
        if curr.key == value:
            return root
        elif curr.key > value:
            curr = root.left
        else:
            curr = root.right
    if parent == None:
        return TreeNode(value)
    elif parent.key > value:
        parent.left = TreeNode(value)
    else:
        parent.right = TreeNode(value)
    return root


@print_return_value
def inorder_traversal(root: TreeNode) -> list[int]:
    # inorder means left > root > right
    result = []
    if root != None:
        inorder_traversal(root.left)
        result.append(root.key)
        inorder_traversal(root.right)
    return result

root1 = TreeNode(9)
root1.left = TreeNode(8)
root1.right = TreeNode(11)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(7)
root1.right.left = TreeNode(12)
root1.right.right = TreeNode(14)

inorder_traversal(root1)

"""

## 9) Validate a Binary Search Tree

**Topic:** BST Fundamentals
**Difficulty:** Medium

Given the root of a binary tree, determine whether it is a valid BST.

A valid BST must satisfy:

* all values in left subtree < node value
* all values in right subtree > node value
* both subtrees must also be valid BSTs

**Example**
Input: `root = [5,1,4,null,null,3,6]`
Output: `False`

**Focus:** Bounds-based recursion, not just parent-child comparison.

---

## 10) Kth Largest Element in an Array

**Topic:** Heap
**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, return the `k`th largest 
element in the array.

**Example**
Input: `nums = [3,2,1,5,6,4], k = 2`
Output: `5`

**Focus:** Min-heap of size `k`, complexity discussion.

---

## Good interview follow-ups for this set

For almost all of these, expect follow-ups like:

* What is the time complexity?
* What is the space complexity?
* Can you do it in-place?
* Can you reduce extra space?
* What edge cases break your code?
* Can you solve it recursively too?

## Suggested solve order

1. Reverse a Singly Linked List
2. Implement Queue Using a Linked List
3. BST Search, Insert, and Inorder Traversal
4. Product of Array Except Self
5. Remove Duplicates From Sorted Array II
6. Validate a BST
7. Reverse Linked List Between Positions
8. Reverse Linked List in Pairs
9. Kth Largest Element in an Array
10. Circular Queue Using Linked List

I can also convert these into a **mock interview sheet with constraints and hints**.

"""