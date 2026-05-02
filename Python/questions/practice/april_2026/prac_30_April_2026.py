from Python.questions.practice.april_2026.prac_24_April_2026 import create_bt
from Python.questions.practice.april_2026.prac_29_April_2026 import print_output


"""
# Set 1

## 1) Two Sum

**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, 
return the indices of the two numbers such that they add 
up to `target`.

You may assume that each input has exactly one solution, 
and you may not use the same element twice.

### Example

**Input:**
`nums = [2,7,11,15], target = 9`
**Output:**
`[0,1]`

---

"""

def two_sum(nums: list[int], target: int) -> list[int]:
    if not nums or not target:
        return []
    start = 0
    end = len(nums) - 1
    result = []
    while start < end:
        two_sum = nums[start] + nums[end]
        if two_sum == target:
            result.append(start)
            result.append(end)
        elif two_sum < target:
            start += 1
        else:
            end -= 1
    return result
"""

## 2) Same Tree

**Difficulty:** Easy

Given the roots of two binary trees `p` and `q`,
write a function to check if they are the same.

Two binary trees are considered the same if 
they are structurally identical and the nodes 
have the same value.

### Example

**Input:**
`p = [1,2,3], q = [1,2,3]`
**Output:**
`true`

---
"""
class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


@print_output
def same_tree(r1: TreeNode, r2: TreeNode) -> bool:
    if r1 is None and  r2 is None:
        return True
    st = [(r1, r2)]

    while st:
        n1, n2 = st.pop()
        
        if n1 is None and n2 is None:
            continue
        
        if n1 is None or n2 is None:
            return False
        
        if n1.key != n2.key:
            return False
        st.append((n1.left, n2.left))
        st.append((n1.right, n2.right))
    return True

bt1 = create_bt([1,2,3, 4])
bt2 = create_bt([1,2,3])


"""

## 3) Best Time to Buy and Sell Stock

**Difficulty:** Easy

You are given an array `prices` where `prices[i]` is the price of 
a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy 
one stock and a different day in the future to sell that stock.

Return the maximum profit you can achieve.

### Example

**Input:**
`prices = [7,1,5,3,6,4]`
**Output:**
`5`

---
"""


@print_output
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if min_price > price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


"""

## 4) Longest Substring Without Repeating Characters

**Difficulty:** Medium

Given a string `s`, find the length of the longest substring without 
repeating characters.

### Example

**Input:**
`s = "abcabcbb"`
**Output:**
`3`

---
"""


@print_output
def longest_substring_without_repeating(s: str | None) -> int:
    if not s:
        return 0
    left = 0
    freq = {}
    b_srt = 0
    b_len = 0
    for right, ch in enumerate(s):
        if ch in freq and freq[ch] >= left:
            left = freq[ch] + 1
        freq[ch] = right
        curr_len = right - left + 1

        if b_len < curr_len:
            b_len = curr_len
            b_srt = left
    return len(s[b_srt:b_srt + b_len])


"""

## 5) Number of Islands

**Difficulty:** Medium

Given an `m x n` grid of `'1'`s and `'0'`s, 
return the number of islands.

An island is surrounded by water and is formed by 
connecting adjacent lands horizontally or vertically.

### Example

**Input:**
`grid = [["1","1","0"],
         ["1","1","0"],
         ["0","0","1"]
        ]`
**Output:**
`2`

---
"""
def dfs(mat: list[list[int]], r: int, c: int) -> None:
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] == "0":
        return
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mat[r][c] = "0"
    for dr, dc in directions:
        dfs(mat, r + dr, c + dc)


@print_output
def number_of_island(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0
    rows = len(mat)
    cols = len(mat[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == "1":
                count += 1
                dfs(mat, r, c)
    return count

number_of_island(
    [["1","1","0"],["1","1","0"],["0","0","1"]]
)

"""

## 6) Design Circular Deque

**Difficulty:** Medium

Design your implementation of the circular double-ended queue.

Implement the `MyCircularDeque` class:

* `MyCircularDeque(k)`
* `insertFront(value)`
* `insertLast(value)`
* `deleteFront()`
* `deleteLast()`
* `getFront()`
* `getRear()`
* `isEmpty()`
* `isFull()`

### Example

**Input:**
`[
"MyCircularDeque",
"insertLast",
"insertLast",
"insertFront","getRear","isFull","deleteLast","insertFront","getFront"]`
`[[3],[1],[2],[3],[],[],[],[4],[]]`

**Output:**
`[null,true,true,true,2,true,true,true,4]`

---
"""
class _Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: _Node | None = None
        self.prev: _Node | None = None



class MyCircularDeque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length: int = 0
        self.head = _Node()
        self.tail = _Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    

    def insertFront(self, value):
        if self.isFull():
            return False
        first = self.head.next
        new_node = _Node(value)
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node
        
        self.length += 1
        return True
        
           
        
    
    def insertLast(self, value):
        if self.isFull():
            return False
        last = self.tail.prev
        new_node = _Node(value)
        new_node.next = self.tail
        self.tail.prev = new_node
        new_node.prev = last

        self.length += 1
        return True


    def deleteFront(self):
        if not self.isEmpty():
            return -1
        first = self.head.next
        second = first.next
        self.head.next = second
        second.prev = self.head
        self.length -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return -1
        last  = self.tail.prev
        last_sec = last.prev
        self.tail.prev = last_sec
        last_sec.next = self.tail
        self.length += 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.head.next.val
    

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.capacity == self.length
        


"""


## 7) Search a 2D Matrix

**Difficulty:** Medium

You are given an `m x n` integer matrix with the following properties:

* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false` otherwise.

### Example

**Input:**
`matrix = [[1,3,5],[7,9,11],[13,15,17]], target = 9`
**Output:**
`true`

---
"""


@print_output
def search_2d_arr(mat: list[list[int]], target: int) -> bool:
    if not mat or not mat[0]:
        return False
    rows = len(mat)
    cols = len(mat[0])
    r = 0
    c = cols - 1
    while 0 <= r < rows and c < cols:
        if mat[r][c] == target:
            return True
        elif mat[r][c] < target:
            r += 1
        else:
            c -= 1
    return False



"""

## 8) Merge Intervals

**Difficulty:** Medium

Given an array of intervals `intervals`, 
merge all overlapping intervals, and return an 
array of the non-overlapping intervals that cover 
all the intervals in the input.

### Example

**Input:**
`intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:**
`[[1,6],[8,10],[15,18]]`

---

"""


@print_output
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    result = []
    intervals.sort()

    prev_start, prev_end = intervals[0]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start <= prev_end:
            prev_end = max(prev_end, end)
        else:
            result.append([prev_start, prev_end])
            prev_start, prev_end = start, end
        
    result.append([prev_start, prev_end])
    return result




"""

## 9) Maximum Sum Subarray of Size K

**Difficulty:** Medium

Given an array of integers `nums` and an integer `k`, 
find the maximum sum of any contiguous subarray of size `k`.

### Example

**Input:**
`nums = [2,1,5,1,3,2], k = 3`
**Output:**
`9`

---
"""


@print_output
def max_subarray_sum(nums: list[int], k: int) -> int:
    if not nums or k == 0:
        return 0
    left = 0 
    # right = k
    prev_sum = sum(nums[left:k])
    max_sum = prev_sum
    for right in range(k, len(nums)):
        curr_sum = prev_sum + nums[right] - nums[left]
        max_sum = max(max_sum, curr_sum)
        left += 1
        prev_sum = curr_sum
    # while right < len(nums):
    #     curr_sum = prev_sum + nums[right] - nums[left]
    #     max_sum = max(max_sum, curr_sum)
    #     left += 1
    #     right += 1
    #     prev_sum = curr_sum
    
    return max_sum

nums = [2,1,5,1,3,2]
k = 3

max_subarray_sum(nums, k)

"""

## 10) Group Anagrams

**Difficulty:** Medium

Given an array of strings `strs`, group the anagrams 
together. You can return the answer in any order.

### Example

**Input:**
`strs = ["eat","tea","tan","ate","nat","bat"]`
**Output:**
`[["bat"],["nat","tan"],["ate","eat","tea"]]`

---

"""


@print_output
def group_anagrams(strs: list[str]) -> list[list[str]]:
    if not strs:
        return []
    freq = {}
    
    for word in strs:
        w = "".join(sorted(word))
        if w in freq:
            freq[w].append(word)
        else:
            freq[w] = [word]
    return list(freq.values())


group_anagrams(["eat","tea","tan","ate","nat","bat"])