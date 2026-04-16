from utils import *
"""
Based on your earlier performance, your main improvement areas look like:

* picking the **exact pattern early**
* **tree recursion helpers** that return structured info
* **design problems** with true `O(1)` operations
* **binary search boundary** questions
* **graph / topo sort**
* **in-place array indexing / cyclic placement**
* cleaner use of **sorted + two pointers** for sum problems

So this set is intentionally chosen to strengthen those weak points.

## Difficulty split

* **2 Easy**
* **7 Medium**
* **1 Hard**

---

## 1) Implement Queue using Stacks

**Topic:** Stack, Design
**Difficulty:** Easy

Implement a first in first out (FIFO) queue using only two stacks.

Implement the `MyQueue` class:

* `push(x)` Push element `x` to the back of queue.
* `pop()` Removes the element from the front of queue and returns it.
* `peek()` Returns the element at the front of queue.
* `empty()` Returns `true` if the queue is empty, `false` otherwise.

### Example 1

**Input:**
`["MyQueue","push","push","peek","pop","empty"]`
`[[],[1],[2],[],[],[]]`

**Output:**
`[null,null,null,1,1,false]`

---

## 2) Diameter of Binary Tree

**Topic:** Tree, DFS
**Difficulty:** Easy

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

### Example 1

**Input:**
`root = [1,2,3,4,5]`
**Output:**
`3`

### Example 2

**Input:**
`root = [1,2]`
**Output:**
`1`


---

## 3) Container With Most Water

**Topic:** Two Pointers
**Difficulty:** Medium

You are given an integer array `height` of length `n`. There are `n` 
vertical lines drawn such that the two endpoints of 
the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the most water.

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


---

## 4) Search Insert Position

**Topic:** Binary Search
**Difficulty:** Medium

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
`nums = [1,3,5,6], target = 5`
**Output:**
`2`

### Example 2

**Input:**
`nums = [1,3,5,6], target = 2`
**Output:**
`1`

### Example 3

**Input:**
`nums = [1,3,5,6], target = 7`
**Output:**
`4`


---

## 5) Find Peak Element

**Topic:** Binary Search
**Difficulty:** Medium

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and 
return its index. If the array contains multiple peaks, return the 
index to any of the peaks.

You must write an algorithm that runs in `O(log n)` time.

### Example 1

**Input:**
`nums = [1,2,3,1]`
**Output:**
`2`

### Example 2

**Input:**
`nums = [1,2,1,3,5,6,4]`
**Output:**
`1`
or
`5`


---

## 6) Validate Binary Search Tree

**Topic:** Tree, BST
**Difficulty:** Medium

Given the `root` of a binary tree, determine if it is a valid binary search tree.

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* Both the left and right subtrees must also be binary search trees.

### Example 1

**Input:**
`root = [2,1,3]`
**Output:**
`true`

### Example 2

**Input:**
`root = [5,1,4,null,null,3,6]`
**Output:**
`false`

### Why this is good for you

You struggled with BST validation before. This is worth revisiting until 
the **range-based helper** feels natural.

---

## 7) Insert Interval

**Topic:** Intervals
**Difficulty:** Medium

You are given an array of non-overlapping intervals `intervals` where 
`intervals[i] = [starti, endi]` represent the start and the end of 
the `i`th interval and `intervals` is sorted in ascending order 
by `starti`. You are also given an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` 
is still sorted in ascending order by `starti` and still does 
not have any overlapping intervals.

Return `intervals` after the insertion.

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

### Why this is good for you

This sharpens your ability to manage **cases and merging logic cleanly**.

---

## 8) Find All Duplicates in an Array

**Topic:** Array, In-place Manipulation
**Difficulty:** Medium

Given an integer array `nums` of length `n` where all the 
integers of `nums` are in the range `[1, n]` and each integer 
appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in `O(n)` time and 
uses only constant extra space.

### Example 1

**Input:**
`nums = [4,3,2,7,8,2,3,1]`
**Output:**
`[2,3]`

### Example 2

**Input:**
`nums = [1,1,2]`
**Output:**
`[1]`

### Why this is good for you

This builds the same mindset needed for **First Missing Positive**.

---

## 9) Course Schedule II

**Topic:** Graphs, Topological Sort
**Difficulty:** Medium

There are a total of `numCourses` courses you have to take, 
labeled from `0` to `numCourses - 1`. You are given an array 
`prerequisites` where `prerequisites[i] = [ai, bi]` indicates 
that you must take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible 
to finish all courses, return an empty array.

### Example 1

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`[0,1]`

### Example 2

**Input:**
`numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
**Output:**
`[0,1,2,3]`
or
`[0,2,1,3]`


---

## 10) Largest Rectangle in Histogram

**Topic:** Stack
**Difficulty:** Hard

Given an array of integers `heights` representing the histogram's bar 
height where the width of each bar is `1`, return the area of the 
largest rectangle in the histogram.

### Example 1

**Input:**
`heights = [2,1,5,6,2,3]`
**Output:**
`10`

### Example 2

**Input:**
`heights = [2,4]`
**Output:**
`4`

### Why this is good for you

This improves your ability to learn a **hard but 
standard pattern**: monotonic stack.

---

# Best order to solve these

Solve in this order for maximum improvement:

1. Implement Queue using Stacks
2. Diameter of Binary Tree
3. Search Insert Position
4. Container With Most Water
5. Validate Binary Search Tree
6. Insert Interval
7. Find All Duplicates in an Array
8. Course Schedule II
9. Find Peak Element
10. Largest Rectangle in Histogram

# What this set targets from your past performance

* **design:** Q1
* **tree helper recursion:** Q2, Q6
* **choosing two pointers correctly:** Q3
* **binary search boundaries / intuition:** Q4, Q9
* **clean interval case handling:** Q7
* **in-place array mapping:** Q8
* **graph topological sort:** Q9
* **hard standard stack pattern:** Q10


"""

# ++++++++++++++++ #
"""
## 1) Implement Queue using Stacks

**Topic:** Stack, Design
**Difficulty:** Easy

Implement a first in first out (FIFO) queue using only two stacks.

Implement the `MyQueue` class:

* `push(x)` Push element `x` to the back of queue.
* `pop()` Removes the element from the front of queue and returns it.
* `peek()` Returns the element at the front of queue.
* `empty()` Returns `true` if the queue is empty, `false` otherwise.

### Example 1

**Input:**
`["MyQueue","push","push","peek","pop","empty"]`
`[[],[1],[2],[],[],[]]`

**Output:**
`[null,null,null,1,1,false]`
"""

class MyQueue:
    """
    Expensive transfers happen rarely, and each element “pays” for its 
    move only once.
    amortized O(1)
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x: int):
        self.in_stack.append(x)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._move()
        return self.out_stack.pop()
    
    def peek(self):
        self._move()
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack


"""
## 2) Diameter of Binary Tree

**Topic:** Tree, DFS
**Difficulty:** Easy

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

### Example 1

**Input:**
`root = [1,2,3,4,5]`
**Output:**
`3`

"""

from ques_13_April_2026 import Node


def height_of_bt(root: Node) -> int:
    if root == None:
        return 0
    else:
        return max(
            height_of_bt(root.left),
            height_of_bt(root.right)
        ) + 1
def diameter_of_bt(root: Node):
    if root == None:
        return 0
    lheight = height_of_bt(root.left)
    rheight = height_of_bt(root.right)

    l_diameter = diameter_of_bt(root.left)
    r_diameter = diameter_of_bt(root.right)

    return max(lheight + rheight, l_diameter, r_diameter)

max_Diameter = 0

def dia_recur(root: Node) -> int:
    if root == None:
        return 0
    global max_Diameter
    lheight = height_of_bt(root.left)
    rheight = height_of_bt(root.right)
    max_Diameter = max(max_Diameter, lheight + rheight)

    return max(lheight, rheight) + 1

def diameter_bt_single_traversal(root: Node) -> int:
    if root == None:
        return
    global max_Diameter
    max_Diameter = 0
    dia_recur(root)
    
    return max_Diameter

"""
## 3) Container With Most Water

**Topic:** Two Pointers
**Difficulty:** Medium

You are given an integer array `height` of length `n`. There are `n` 
vertical lines drawn such that the two endpoints of 
the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the most water.

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
"""

def max_water(heights: list[int]) -> int:
    if not heights:
        return 0
    n = len(heights)
    left, right = 0, n - 1
    max_capcity = 0
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_capcity = max(max_capcity, height * width)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_capcity

"""
## 4) Search Insert Position

**Topic:** Binary Search
**Difficulty:** Medium

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1

**Input:**
`nums = [1,3,5,6], target = 5`
**Output:**
`2`

### Example 2

**Input:**
`nums = [1,3,5,6], target = 2`
**Output:**
`1`

### Example 3

**Input:**
`nums = [1,3,5,6], target = 7`
**Output:**
`4`
"""

def search_target_return_idx(nums: list[int], target: int) -> int:
    if not nums:
        return 0
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

"""
---

## 5) Find Peak Element

**Topic:** Binary Search
**Difficulty:** Medium

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and 
return its index. If the array contains multiple peaks, return the 
index to any of the peaks.

You must write an algorithm that runs in `O(log n)` time.

### Example 1

**Input:**
`nums = [1,2,3,1]`
**Output:**
`2`

### Example 2

**Input:**
`nums = [1,2,1,3,5,6,4]`
**Output:**
`1`
or
`5`

"""
@print_return_value
def find_maxima_bt(nums: list[int]) -> int:
    """
    key intuition to look for slope are you on increasing or decreasing slope
    """
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

"""
## 6) Validate Binary Search Tree

**Topic:** Tree, BST
**Difficulty:** Medium

Given the `root` of a binary tree, determine if it is a valid binary search tree.

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* Both the left and right subtrees must also be binary search trees.

### Example 1

**Input:**
`root = [2,1,3]`
**Output:**
`true`

### Example 2

**Input:**
`root = [5,1,4,null,null,3,6]`
**Output:**
`false`

"""
def inorder(root: Node, prev: int) -> bool:
    if root is None:
        return True
    if not inorder(root.left):
        return False
    if prev is not None and root.key <= prev:
        return False
    prev = root.key
    return inorder(root.right, prev)

@print_return_value
def valid_bst(root: Node) -> bool:
    prev = None
    return inorder(root, prev)


@print_return_value
def list_based_valid_dfs(nums: list[int | None]) -> bool:
    def list_based_dfs(idx: int, low: int, high: int) -> bool:
        if idx >= len(nums) or nums[idx] == None:
            return True
        val = nums[idx]
        if not (low < val < high):
            return False
        left = 2 * idx + 1
        right = 2 * idx + 2
        return list_based_dfs(left, low, val) and list_based_dfs(right, val, high)
    return list_based_dfs(0, float("-inf"), float("inf"))


"""
## 7) Insert Interval

**Topic:** Intervals
**Difficulty:** Medium

You are given an array of non-overlapping intervals `intervals` where 
`intervals[i] = [starti, endi]` represent the start and the end of 
the `i`th interval and `intervals` is sorted in ascending order 
by `starti`. You are also given an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` 
is still sorted in ascending order by `starti` and still does 
not have any overlapping intervals.

Return `intervals` after the insertion.

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

### Why this is good for you

This sharpens your ability to manage **cases and merging logic cleanly**.

"""
@print_return_value
def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals completely before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge all overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    # 3. Add the merged new_interval
    result.append(new_interval)

    # 4. Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
    

"""
## 9) Course Schedule II

**Topic:** Graphs, Topological Sort
**Difficulty:** Medium

There are a total of `numCourses` courses you have to take, 
labeled from `0` to `numCourses - 1`. You are given an array 
`prerequisites` where `prerequisites[i] = [ai, bi]` indicates 
that you must take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible 
to finish all courses, return an empty array.

### Example 1

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`[0,1]`

### Example 2

**Input:**
`numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
**Output:**
`[0,1,2,3]`
or
`[0,2,1,3]`

"""
from collections import deque

@print_return_value
def course_finish_order(numCourses, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(numCourses)}
    indegrees = [0] * numCourses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegrees[course] += 1
    order = []
    q = deque()
    for i in range(numCourses):
        if indegrees[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        order.append(node)
        for n in graph[node]:
            indegrees[n] -= 1
            if indegrees[n] == 0:
                q.append(n)
    return order if len(order) == numCourses else []

"""
## 8) Find All Duplicates in an Array

**Topic:** Array, In-place Manipulation
**Difficulty:** Medium

Given an integer array `nums` of length `n` where all the 
integers of `nums` are in the range `[1, n]` and each integer 
appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in `O(n)` time and 
uses only constant extra space.

### Example 1

**Input:**
`nums = [4,3,2,7,8,2,3,1]`
**Output:**
`[2,3]`

### Example 2

**Input:**
`nums = [1,1,2]`
**Output:**
`[1]`
"""
@print_return_value
def find_all_duplicates(nums: list[int]) -> list[int]:
    result = []
    # use array like a visitation record mark all visited
    # element as negative:
    for num in nums:
        idx = abs(num) - 1

        if nums[idx] < 0:
            # it means already visisted.
            result.append(abs(num))
        else:
            # mark visited 
            nums[idx] = -nums[idx]
    
    return result
    



"""
## 10) Largest Rectangle in Histogram

**Topic:** Stack
**Difficulty:** Hard

### Example 1

**Input:**
`heights = [2,1,5,6,2,3]`
**Output:**
`10`

### Example 2

**Input:**
`heights = [2,4]`
**Output:**
`4`

"""

@print_return_value
def largest_rectangle_hestogram(heights: list[int]) -> int:
    if not heights:
        return 0
    max_area = 0
    stack = []
    # append 0 at the end to force start processing heights
    heights.append(0)
    for i in range(len(heights)):
        # while current height is less that previous height stop and
        # calcualte area
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            # for empty stack width start from 0 
            if not stack:
                width = i
            else: 
                width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    # optional clean up
    stack.pop()
    return max_area

if __name__ == "__main__":
  largest_rectangle_hestogram([2,1,5,6,2,3])