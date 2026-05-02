from collections import deque

from utils import (
    print_output, 
    create_bt, 
    TreeNode, 
    ListNode,
    create_ll,
)

"""
# Set 2

## 1) Valid Palindrome

**Difficulty:** Easy

Given a string `s`, determine if it is a palindrome after 
converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters.

### Example

**Input:**
`s = "A man, a plan, a canal: Panama"`
**Output:**
`true`

---
"""

@print_output
def valid_palindrome(s: str) -> bool:
    if not s:
        return True
    srt = 0
    end = len(s) - 1
    s = s.lower()
    while srt < end:
        while srt < end and not s[end].isalnum():
            end -= 1
        while srt < end and not s[srt].isalnum():
            srt += 1
        if s[srt] != s[end]:
            return False
        
        srt += 1
        end -= 1
    return True


# valid_palindrome("A man, a plan, a canal: Panama")

"""

## 2) Remove Duplicates from Sorted Array

**Difficulty:** Easy

Given an integer array `nums` sorted in non-decreasing order,
remove the duplicates in-place such that each unique element 
appears only once.

Return the number of unique elements.

### Example

**Input:**
`nums = [1,1,2]`
**Output:**
`2`

---
"""


@print_output
def remove_duplicates_from_sorted_arr(nums: list[int]) -> int:
    if not nums:
        return 0
    left = 0

    for right in range(1, len(nums)):
        if nums[right] != nums[left - 1]:
            nums[left] = nums[right]
            left += 1

    return left


# remove_duplicates_from_sorted_arr([1, 1, 2, 3 , 3, 3, 4, 4 , 4, 5, 6 , 7, 7 , 7 , 7 , 8, 8])

"""

## 3) Search in a Binary Search Tree

**Difficulty:** Easy

You are given the root of a binary search tree and an integer `val`.

Find the node in the BST whose value equals `val` and return the subtree 
rooted with that node. If such a node does not exist, return `null`.

### Example

**Input:**
`root = [4,2,7,1,3], val = 2`
**Output:**
`[2,1,3]`

---
"""

def search_in_bt(root: TreeNode, val: int) -> TreeNode | None:
    if root is None:
        return root
    curr = root
    while curr:
        if curr.key == val:
            print(curr.key)
            return curr
        elif curr.key > val:
            curr = curr.left
        else:
            curr = curr.right
    return 



bt1 = create_bt([4,2,7,1,3])

# search_in_bt(bt1, 2)
"""

## 4) Spiral Matrix

**Difficulty:** Medium

Given an `m x n` matrix, return all elements of 
the matrix in spiral order.

### Example

**Input:**
`matrix = [[1,2,3],
           [4,5,6],
           [7,8,9]]`
**Output:**
`[1,2,3,6,9,8,7,4,5]`

---
"""


@print_output
def spiral_matrix(mat: list[list[int]]) -> list[int]:
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1
    result = []
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right , left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    return result


# spiral_matrix([[1,2,3],[4,5,6],[7,8,9]])
"""


## 5) Container With Most Water

**Difficulty:** Medium

You are given an integer array `height`. 
Find two lines that together with the x-axis 
form a container that holds the most water.

Return the maximum amount of water a container can store.

### Example

**Input:**
`height = [1,8,6,2,5,4,8,3,7]`
**Output:**
`49`

---

"""

@print_output
def container_with_most_water(height: list[int]) -> int:
    if not height:
        return 0
    start = 0
    end = len(height) - 1
    max_water = 0
    while start < end:
        h = min(height[start], height[end])
        w = end - start
        curr_water = h * w
        max_water = max(max_water, curr_water)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return max_water



# container_with_most_water([1,8,6,2,5,4,8,3,7])
"""

## 6) Search Insert Position

**Difficulty:** Medium

Given a sorted array of distinct integers and a target value, 
return the index if the target is found.

If not, return the index where it would be inserted in order.

### Example

**Input:**
`nums = [1,3,5,6], target = 5`
**Output:**
`2`

---
"""


@print_output
def search_index_pos(nums: list[int], target: int) -> int | None:
    if not nums:
        return None
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# search_index_pos([1,3,5,6], 7)

"""

## 7) Find Peak Element

**Difficulty:** Medium

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of them.

### Example

**Input:**
`nums = [1,2,3,1,0, 2, 4, 3, 1]`
**Output:**
`2`

---
"""


@print_output
def find_peak_element(nums: list[int]) -> int:
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left  # or right 


# find_peak_element([0, 1, 2, 3, 4, 1])
"""

## 8) Relative Sort Array

**Difficulty:** Medium

Given two arrays `arr1` and `arr2`, sort the elements of `arr1` such that:

* the relative ordering of items in `arr1` are the same as in `arr2`
* elements not in `arr2` are placed at the end in ascending order

### Example

**Input:**
`arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]`
**Output:**
`[2,2,2,1,4,3,3,9,6,7,19]`

---

"""


@print_output
def relative_sort_arr(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1 or not arr2:
        return arr1 or arr2
    freq = {}
    result = []
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        result.extend([num] * freq[num])
        del freq[num]
    remaining = []

    for num, cnt in freq.items():
        remaining.extend([num] * cnt)
    result.extend(remaining)
    
    return result


# relative_sort_arr([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])    

"""

## 9) Palindrome Linked List

**Difficulty:** Medium

Given the head of a singly linked list, return `true` if it is a 
palindrome or `false` otherwise.

### Example

**Input:**
`head = [1,2,2,1]`
**Output:**
`true`

---
"""


@print_output
def palindrome_linked_list(head: ListNode) -> bool:
    if head is None:
        return True
    
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # skip if odd length list
    if fast:
        slow = slow.next

    curr = slow
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    first = head
    second = prev

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True


ll1 = create_ll([1,2,2,1, 1])
# palindrome_linked_list(ll1)
"""

## 10) Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

Given the root of a binary tree, return the zigzag level 
order traversal of its nodes’ values.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[20,9],[15,7]]`

---
"""


@print_output
def bst_zig_zag_level_order_traversal(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    q = deque([root])
    result = []
    right_to_left = True
    while q:
        l_size = len(q)
        levl = deque()
        for _ in range(l_size):
            node = q.popleft()
            if right_to_left:
                levl.append(node.key)
            else:
                levl.appendleft(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(list(levl))
        right_to_left = not right_to_left
    return result


bt2 = create_bt([3,9,20,None,None,15,7])

bst_zig_zag_level_order_traversal(bt2)