

"""
---

## 1) Min Stack

**Topic:** Stack, Design
**Difficulty:** Easy

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

* `MinStack()` initializes the stack object.
* `push(val)` pushes the element `val` onto the stack.
* `pop()` removes the element on the top of the stack.
* `top()` gets the top element.
* `getMin()` retrieves the minimum element in the stack.

### Example 1

**Input:**
`["MinStack","push","push","push","getMin","pop","top","getMin"]`
`[[],[-2],[0],[-3],[],[],[],[]]`

**Output:**
`[null,null,null,null,-3,null,0,-2]`

### Constraints

* `-2^31 <= val <= 2^31 - 1`
* Methods `pop`, `top`, and `getMin` operations will always be called on non-empty stacks.

---

## 2) Balanced Binary Tree

**Topic:** Tree, Binary Tree
**Difficulty:** Easy

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`true`

### Example 2

**Input:**
`root = [1,2,2,3,3,null,null,4,4]`
**Output:**
`false`

### Constraints

* The number of nodes in the tree is in the range `[0, 5000]`
* `-10^4 <= Node.val <= 10^4`

---

## 3) 3Sum

**Topic:** Array, Sorting, Two Pointers
**Difficulty:** Medium

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

### Example 1

**Input:**
`nums = [-1,0,1,2,-1,-4]`
**Output:**
`[[-1,-1,2],[-1,0,1]]`

### Example 2

**Input:**
`nums = [0,1,1]`
**Output:**
`[]`

### Constraints

* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

---

## 4) Group Anagrams

**Topic:** Hashing, Strings, Array
**Difficulty:** Medium

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word formed by rearranging the letters of another word.

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

### Constraints

* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`

---

## 5) Reorder List

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium

You are given the head of a singly linked-list. Reorder the list to be on the following form:

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

You may not modify the values in the list’s nodes. Only nodes themselves may be changed.

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

### Constraints

* The number of nodes in the list is in the range `[1, 5 * 10^4]`
* `1 <= Node.val <= 1000`

---

## 6) Find First and Last Position of Element in Sorted Array

**Topic:** Searching, Binary Search
**Difficulty:** Medium

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

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

### Constraints

* `0 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## 7) Task Scheduler

**Topic:** Heaps, Greedy, Hashing
**Difficulty:** Medium

You are given an array of CPU tasks, each represented by a character 
from `A` to `Z`, and a cooling time `n`.

Each cycle or interval allows the completion of one task. 
Tasks can be completed in any order, but there must be at least 
`n` intervals between two same tasks.

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

### Constraints

* `1 <= tasks.length <= 10^4`
* `tasks[i]` is an uppercase English letter
* `0 <= n <= 100`

---

## 8) Course Schedule

**Topic:** Graphs, Topological Sort, DFS/BFS
**Difficulty:** Medium

There are a total of `numCourses` courses you have to take, 
labeled from `0` to `numCourses - 1`.

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` 
indicates that you must take course `bi` first if you want to take course `ai`.

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
* `0 <= prerequisites.length <= 5000`

---

## 9) Spiral Matrix

**Topic:** Matrices, Simulation
**Difficulty:** Medium

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Example 1

**Input:**
`matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:**
`[1,2,3,6,9,8,7,4,5]`

### Example 2

**Input:**
`matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
**Output:**
`[1,2,3,4,8,12,11,10,9,5,6,7]`

### Constraints

* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

---

## 10) First Missing Positive

**Topic:** Array, In-place Manipulation
**Difficulty:** Hard

Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

### Example 1

**Input:**
`nums = [1,2,0]`
**Output:**
`3`

### Example 2

**Input:**
`nums = [3,4,-1,1]`
**Output:**
`2`

### Example 3

**Input:**
`nums = [7,8,9,11,12]`
**Output:**
`1`

### Constraints

* `1 <= nums.length <= 10^5`
* `-2^31 <= nums[i] <= 2^31 - 1`

---

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

"""
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

* `MinStack()` initializes the stack object.
* `push(val)` pushes the element `val` onto the stack.
* `pop()` removes the element on the top of the stack.
* `top()` gets the top element.
* `getMin()` retrieves the minimum element in the stack.
"""

class MinStack:
    # core logic:
    # - min_val will be recalculated whenever a new element will be added to stack
    # constructor : init a empty list, min_val = None | 0
    # methods/behaviour
    # push(val) >> append val to self.stack
    # pop() >> pop top element from self.stack 
    # top() return top value from self.stack e.g return self.stack[0]
    # getMin() >> return self.min_val 
    def __init__(self):
        self.stack: list = []
        self.min_val: int = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 0:
            for v in self.stack:
                self.min_val = min(self.min_val, v)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
    
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.min_val
    
"""
## 2) Balanced Binary Tree

**Topic:** Tree, Binary Tree
**Difficulty:** Easy

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`true`

### Example 2

**Input:**
`root = [1,2,2,3,3,null,null,4,4]`
**Output:**
`false`

### Constraints

* The number of nodes in the tree is in the range `[0, 5000]`
* `-10^4 <= Node.val <= 10^4`
"""
#   
# Learning : learn to work with list based trees .
#

def balanced_bst(root: Node) -> bool:
    # code logic : 
    # will calculate the height/depth or each subtree recursively and return True
    # if just differ by 1 else False
    if root == None:
        return 0
    else:
        if (balanced_bst(root.left) + 1) - (balanced_bst(root.right) + 1) > 1:
            return False
        else:
            return True
        
"""
## 3) 3Sum

**Topic:** Array, Sorting, Two Pointers
**Difficulty:** Medium

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

### Example 1

**Input:**
`nums = [-1,0,1,2,-1,-4]`
**Output:**
`[[-1,-1,2],[-1,0,1]]`

### Example 2

**Input:**
`nums = [0,1,1]`
**Output:**
`[]`

### Constraints

* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

"""

def three_sum(arr: list[int]) -> list[list[int]]:
    # core logic:
    # sort the array  
    # will be using two pointer to track two element and use a set to keep 
    # diff/already calculated num
    # later fell on sliding window, problem with sliding window is it calculate
    # only consecutive elements
    if not arr:
        return arr
    resp = []
    arr.sort()
    n = len(arr)
    left = 0
    right = 2
    
    while right < n:
        if arr[left] + arr[left + 1] + arr[right] == 0:
           resp.append([arr[left], arr[left + 1], arr[right]])
           left += 1
           right += 1
        else:
            left += 1
            right += 1
    return resp


"""
## 4) Group Anagrams

**Topic:** Hashing, Strings, Array
**Difficulty:** Medium

Given an array of strings `strs`, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word formed by rearranging the letters of another word.

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

### Constraints

* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    if not words:
        return words
    u_map = {} # {"aet": ["eat", "tea"]}
    resp = []
    for w in words:
        s = "".join(sorted(w))
        if s in u_map:
            u_map[s].append(w)
        else:
            u_map[s] = [w]
    for key in u_map.values():
        resp.append(key)
    # or return list(u_map.values())
    return resp

"""
## 5) Reorder List

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium

You are given the head of a singly linked-list. Reorder the list to be on the following form:

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

You may not modify the values in the list’s nodes. Only nodes themselves may be changed.

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

### Constraints

* The number of nodes in the list is in the range `[1, 5 * 10^4]`
* `1 <= Node.val <= 1000`
"""

def reorder_linklist(head: ListNode) -> ListNode:
    if not head:
        return head
    slow = head
    fast = head
    # 1 find middle of the linkedlist
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2 detach from middle and reverse half of linklist 
    curr = slow.next
    prev = None
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    # 3 Interleave and Merge

    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
    return head


"""
## 6) Find First and Last Position of Element in Sorted Array

**Topic:** Searching, Binary Search
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

### Constraints

* `0 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`
"""


"""
## 9) Spiral Matrix

**Topic:** Matrices, Simulation
**Difficulty:** Medium

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Example 1

**Input:**
`matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:**
`[1,2,3,6,9,8,7,4,5]`

### Example 2

**Input:**
`matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
**Output:**
`[1,2,3,4,8,12,11,10,9,5,6,7]`

### Constraints

* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`
"""

def print_matrix_spiral(mat: list[list[int]]) -> None:
    if not mat or not mat[0]:
        return None
    rows = len(mat)
    cols = len(mat[0])
    top = 0
    left = 0
    bottom = rows - 1
    right = cols - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(mat[top][i], end=" ")
        top += 1
        for i in range(top, bottom + 1):
            print(mat[i][right], end=" ")
        right -= 1
        if top <= bottom: 
            for i in range(right, left - 1 , -1):
                print(mat[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1 , -1):
                print(mat[i][left], end=" ")
            left += 1

if __name__ == "__main__":
    print_matrix_spiral(
        [[1,2,3],[4,5,6],[7,8,9]]
    )