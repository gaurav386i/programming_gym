from heapq import heappush, heappop
from collections import deque

from prac_24_April_2026 import create_bt


def print_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)

        return result
    return wrapper


"""

---

## 1) Backspace String Compare

**Difficulty:** Easy

Given two strings `s` and `t`, return `true` if they are equal when both are 
typed into empty text editors. `'#'` means a backspace character.

### Example 1

**Input:**
`s = "ab#c", t = "ad#c"`
**Output:**
`true`

### Example 2

**Input:**
`s = "a#c", t = "b"`
**Output:**
`false`

---
"""

@print_output
def backspace_string_compare(s: str, t: str) -> bool:
    if not s or not t: 
        return False
    def build(word: str) -> str:
        st = []
        for ch in word:
            if ch == "#":
                if st:
                    st.pop()
            else:
                st.append(ch)
        return st

    return  len(build(s)) == len(build(t))



"""

## 2) 3Sum

**Difficulty:** Medium

Given an integer array `nums`, return all the unique triplets 
`[nums[i], nums[j], nums[k]]` such that:

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

---
"""
@print_output
def three_sum(nums: list[int]) -> list[list[int]]:

    if not nums:
        return []
    # sort for 2 pointer to work in three pointers setup 
    nums.sort()
    resp = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                resp.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return resp




"""

## 3) Daily Temperatures

**Difficulty:** Medium

Given an array of integers `temperatures` representing the daily 
temperatures, return an array `answer` such that `answer[i]` 
is the number of days you have to wait after the `i`th day to 
get a warmer temperature. If there is no future day, keep `answer[i] = 0`.

### Example 1

**Input:**
`temperatures = [73,74,75,71,69,72,76,73]`
**Output:**
`[1,1,4,2,1,1,0,0]`

### Example 2

**Input:**
`temperatures = [30,40,50,60]`
**Output:**
`[1,1,1,0]`

---
"""

@print_output
def daily_temperature(temperatures: list[int]) -> list[int]:
    if not temperatures:
        return []
    st = []
    result = [0] * len(temperatures)
    for daily in range(len(temperatures)):
        while st and temperatures[daily] > temperatures[st[-1]]:
            prev_temp = st.pop()
            result[prev_temp] = daily - prev_temp
        st.append(daily)
       
    return result

daily_temperature([73,74,75,71,69,72,76,73])


"""

## 4) Validate Binary Search Tree

**Difficulty:** Medium

Given the root of a binary tree, determine if it is a valid binary search tree.

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node’s key.
* The right subtree contains only nodes with keys greater than the node’s key.
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

---
"""
class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


@print_output
def validate_bst(root: TreeNode) -> bool:
    def dfs(node: TreeNode, low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.key < high):
            return False
        else:
            return dfs(node.left, low, node.key) and dfs(node.right, node.key, high)
    return dfs(root, float("-inf"), float("inf"))

@print_output
def validate_st_bst(root: TreeNode) -> bool:
    if root is None:
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
     


bt1 = create_bt([2,1,3])

validate_st_bst(bt1)

"""

## 5) Find K Pairs with Smallest Sums

**Difficulty:** Medium

You are given two integer arrays `nums1` and `nums2` 
sorted in ascending order and an integer `k`.

Define a pair `(u, v)` where one element is from 
the first array and the other is from the second array.

Return the `k` pairs with the smallest sums.

### Example 1

**Input:**
`nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
**Output:**
`[[1,2],[1,4],[1,6]]`

### Example 2

**Input:**
`nums1 = [1,1,2], nums2 = [1,2,3], k = 2`
**Output:**
`[[1,1],[1,1]]`

"""

@print_output
def k_pair_with_smallest_sum(nums1: list[int], nums2: list[int], kth: int) -> list[list[int]]:
    if not nums1 or not nums2 or kth == 0:
        return []
    min_h = []
    result = []
    for i in range(min(len(nums1), kth)):
        pair_sum = nums1[i] + nums2[0]
        heappush(min_h, (pair_sum, i, 0 ))
    count = 0
    while min_h and count < kth:
        _, n1_idx, n2_idx = heappop(min_h)
        result.append([nums1[n1_idx], nums2[n2_idx]])
        
        if n2_idx + 1 < len(nums2):
            pair_sum = nums1[n1_idx] + nums2[n2_idx + 1]
            heappush(min_h, (pair_sum, n1_idx, n2_idx + 1))
        count += 1
        
    
    return result

k_pair_with_smallest_sum([1,7,11], [2,4,6], 3 )



        
    
"""


"""