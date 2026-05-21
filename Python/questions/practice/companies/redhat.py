from collections import deque

"""
---

## 1. Design Sparse Vector

**Design a data structure to efficiently store and compute the dot product of two sparse vectors.**

A sparse vector is a vector that has mostly zero values. You should implement the `SparseVector` class:

* `SparseVector(nums)`: Initializes the object with the vector `nums`.
* `dotProduct(vec)`: Compute the dot product between the instance of `SparseVector` and `vec`.

A **dot product** of two vectors $v_1 = [a_1, a_2, ..., a_n]$ and $v_2 = [b_1, b_2, ..., b_n]$ is defined as:


$$\sum_{i=1}^{n} a_i \cdot b_i$$

**Example:**

```text
Input: nums1 = [1, 0, 0, 2, 3], nums2 = [0, 3, 0, 4, 0]
Output: 8
Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

```
---
What is a spart vector ?
What if a vector is completely zeros , how we handle it 
Is there a size limitation of the input
assumptions :
1. SparseVector class contains:
   1. contructor
   2. Dot product
   Constructor which take spart vector list[int's] as input and create sparce vector object
   DotProduct consumes incoming vector and resturn dot product of both spvector object one which 
   dot product is invoked and consumed spvec
"""

class SparseVector:
    def __init__(self, vector: list[int]):
        self.sp_vec: dict = {i: num for i, num in enumerate(vector) if num != 0}

    def dot_product(self, vec: "SparseVector") -> float:
        
        if len(self.sp_vec) > len(vec.sp_vec):
            small_vec, big_vec = vec.sp_vec, self.sp_vec
        else:
            small_vec, big_vec = self.sp_vec, vec.sp_vec
        result = 0
        for k, v in small_vec.items():
            if k in big_vec:
                result += v * big_vec[k]
            
        
        return result






"""

## 2. Validate Binary Search Tree

**Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).**

A **valid BST** is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.

**Constraints:**

* The number of nodes in the tree is in the range $[1, 10^4]$.
* $-2^{31} \le Node.val \le 2^{31} - 1$

---
requirements:
What if input is not provided. what will be height and depth of the tree
assumptions :
Input will be a tree or None, its height and depth will be finite 

core logic : try recursive first : if node sits between float("-inf") and float("inf"), recursively call
             validate_bst(root left child, float("-inf"), root' key) and validate_bst(root right child, 
             root' key, float("inf"))
improve by trying to implement stack or level order traversal using bfs 
"""
class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def validate_bt(root: TreeNode) -> bool:
    if not root:
        return True
    def bfs(node, low: float, high: float) -> bool:
        if not (low < node.key < high):
            return False
        else:
            return bfs(node.left, low, node.key) and bfs(node.right, node.key, high)
    return bfs(root, float("-inf"), float("inf"))


def itr_validate_bst(root: TreeNode):
    if not root:
        return True
    st = [(root, float("-inf"), float("inf"))]
    while st:
        node, low, high = st.pop()
        if not (low < node.key < high):
            return False
        if node.left is not None:
            st.append((node.left, low, node.key))
        if node.right is not None:
            st.append((node.right, node.key, high))
    return True

"""

## 3. Middle of the Linked List

**Given the `head` of a singly linked list, return the middle node of the linked list.**

If there are two middle nodes, return the **second middle** node.

**Example:**

```text
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]
Explanation: The middle node of the list is 3.

Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

```
requirements and assumptions :
how to handle if input is not provided , or single node , need to handle even and odd ll
assumptions: 
           input is a valid ll or None , will return middle of linked list , 
core logic : 
naive : will iterate the whole linked lisk calcualte the length, use the length to reach the middle of 
        ll and return it .

efficient : use two pointer slow and fast when fast reaches end slow will be in middle if we do 
            fast = 2 X slow 


---
"""
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None

def middle_of_ll(head: Node) -> Node:
    if not head or head.next is None:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    return slow
"""


## 4. Linked List Cycle Detection

**Given `head`, the head of a linked list, determine if the 
linked list has a cycle in it.**

There is a cycle in a linked list if there is some node in the 
list that can be reached again by continuously following the `next` pointer.

**Follow up:** Can you solve it using $O(1)$ (i.e., constant) memory?

# requirements and asssumptions :
what if input is None or head only , what if there is no cycle .
assumptions :
innput is a valid ll node or None, linked maybe having cycle or not .
size of ll is finite 

Core idea : naive approach run a loop of next on ll if it stuck for ever ll got a cycle.
efficient : user two slow and fast pointers if they meet again before fast pointing to None ll got a cycle

---
"""

def detect_cycle_in_ll(head: Node) -> bool:
    if not head or head.next is None:
        return False
    slow = fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         return True
    # return False
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

"""


## 5. Implement Stack using Queues

**Implement a last-in-first-out (LIFO) stack using only two queues.**

The implemented stack should support all the functions of a normal 
stack (`push`, `top`, `pop`, and `empty`).

**Notes:**

* You must use only standard operations of a queue (push to back, 
peek/pop from front, size, and is empty).
* Depending on your language, the queue may not be supported natively. 
You may use a list or deque (double-ended queue) as long as you use only 
a queue's standard operations.

requirements and assumptions :
requirements: what is the expectation for space and time complexities of operations,
              should it support a specific type of data or any type of data/objects
              Is there is any size or capacity requirements or constraints
              what to return if stack is empty for pop/ top operations
core logic : I will be using two deques for MyStack implemetation i.e in_queue and out_queue
             append inputs in in_queue, then append all existing element from out_queue to in_queue
             once done swap the values of both queue .

---
"""
class MyStack:
    def __init__(self):
        self.in_q = deque()
        self.out_q = deque()
    
    def push(self, value: int) -> int:
        self.in_q.append(value)
        while self.out_q:
            self.in_q.append(self.out_q.popleft())
        self.out_q, self.in_q = self.in_q, self.out_q
    
    def pop(self) -> int:
        if self.empty():
            return None
        return self.out_q.popleft()
    
    def top(self) -> int:
        if self.empty():
            return None
        return self.out_q[0]
    
    def empty(self) -> bool:
        return not self.out_q
        
            
"""

## 6. Intersection of Two Linked Lists

**Given the heads of two singly linked-lists `headA` and `headB`, 
return the node at which the two lists intersect.**

If the two linked lists have no intersection at all, return `null`.

**Constraints:**

* The list must retain its original structure after the function returns.
* Your solution should ideally run in $O(n)$ time and use $O(1)$ space.
requirements and assumptions :
what is intersection in terms of linked list I guess node exits in both linked lists 
what is one linked is missing from out or both are missing from out . what is size of both 
linked list 
assumptions : 
both inputt are eaither valid ll or None , length of both linked list are finite
core login :
           declare two pointers which point to head of both ll respectively, iterate over 
           these pointer until both pointers become equal/start pointing to same node
           if pointer reaches end of ll or met .
---
"""

def find_intersection_of_two_ll(headA: Node, headB: Node) -> Node:
    if not headA or not headB:
        return None
    pA = headA
    pB = headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA
"""

## 7. Sort Binary Array

**Given a binary array `nums` containing only $0$s and $1$s, sort the array in-place.**

**Constraints:**

* Time Complexity: $O(n)$
* Space Complexity: $O(1)$

**Example:**

```text
Input: nums = [1, 0, 1, 1, 0, 0, 1]
Output: [0, 0, 0, 1, 1, 1, 1]

```
requirements and assumptions 
reqs : what to return if input is None or empty list , did this list will contains anything other that 0 and 1
assumptions : 
            imput is a list of 0 and 1 or None , length of list will be finite and no other literals will allowed in 
            list except 0 & 1 , time complexity of solution will be O(n) and required space will be O(1). 
---
"""

def sort_binary_array(nums: list[int]) -> list[int]:
    if not nums:
        return []
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
            left += 1
        else:
            right += 1
    return nums

"""

## 8. Maximum Subarray (Kadane’s Algorithm)

**Given an integer array `nums`, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.**

**Example:**

```text
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

```

---
"""

def max_contiguous_sub_arr_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]

    for n in nums:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum
"""

## 9. Sort Colors (0s, 1s, and 2s)

**Given an array `nums` with $n$ objects colored red, white, or 
blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.**

We will use the integers $0$, $1$, and $2$ to represent the color red, white, 
and blue, respectively.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

---
"""
def sort_colors(colors: list[int]) -> list[int]:
    if not colors:
        return []
    
    left = 0
    mid = 0
    right = len(colors) - 1
    while mid <= right:
        if colors[mid] == 0:
            colors[left], colors[mid] = colors[mid], colors[left]
            mid += 1
            left += 1
        elif colors[mid] == 1:
            mid += 1
        else:  # colors[mid] == 2
            colors[right], colors[mid] = colors[mid], colors[right]
            mid += 1
            right -= 1
    
    return colors

    
"""

## 10. Add Two Numbers

**You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.**

Add the two numbers and return the sum as a linked list.

**Example:**

```text
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807.

```

---
"""

def add_two_ll(l1: Node, l2: Node) -> Node:
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = Node(0)
    tail = dummy
    carry = 0
    while l1 or l2 or carry:
        val1= l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        total = val1 + val2 + carry
        
        tail.next = Node(total % 10)
        l1 = l1.next
        l2 = l2.next
        carry = total // 10
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next


"""

## 11. Binary Tree Spiral Order Traversal

**Given the `root` of a binary tree, return the spiral level order 
traversal of its nodes' values.**

(i.e., from left to right, then right to left for
 the next level and alternate between).

**Example:**

```text
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]

```
---
"""
def spiral_bt_traversal(root: TreeNode) -> list[list[int]]:
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
        result.append(list(level))
        left_to_right = not left_to_right
    
    return result
"""

## 12. Edit Distance (String Transformation)

**Given two strings `word1` and `word2`, return the minimum number of 
operations required to convert `word1` to `word2`.**

You have the following three operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

**Example:**

```text
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

---

## 13. Lowest Common Ancestor of a Binary Tree

**Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.**

The LCA is defined between two nodes $p$ and $q$ as the lowest node in $T$ that 
has both $p$ and $q$ as descendants (where we allow a node to be a descendant of itself).

---
What if both or either of p and q is not given .
both p and q are binary trees, which on p & q we suppose as left and right child
What it means "when we say > Where we allow a node to be a descendant of itself."

 assumptions : lowest both p & q will be either a valid binary tree or None , root of binary 
               in which are going to search is a valid bst or None
Core Logic : 
           if we will handle edge case either both p or q or root is None 
           then will check if root.left  and root.right are equal to p or q

"""

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root ==  p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right :
        return root
    return left if left else right
"""

## 14. Family Tree Modeling

**Model a family tree using a graph data structure.**

Implement a class `FamilyTree` that supports:

1. `add_parent(child, parent)`: Establishes a directed relationship.
2. `is_ancestor(a, b)`: Returns `True` if `a` is an ancestor of `b`.
3. `find_common_ancestors(a, b)`: Returns a list of all shared ancestors.

**Considerations:** Handle cycles (though biologically impossible, the code should be robust) 
and disconnected components.

---

## 15. Integer to String (itoa)

**Implement a function to convert an integer to a string without using 
built-in conversion functions (like `str()` in Python or `sprintf` in C).**

You should handle:

* Negative numbers.
* The number zero.
* Standard variable types and basic digit mapping.

**Example:**

```text
Input: -123
Output: "-123"

```
"""


if __name__ == "__main__":
    # print(sort_binary_array([1, 0, 1, 1, 0, 0, 1]))
    # print(sort_colors([2,0,2,1,1,0]))
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
    print(v1.dot_product(v2))