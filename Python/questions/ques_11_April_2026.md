
---

## 1) Two Sum

**Topic:** Array, Hashing
**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use the same element twice.

### Example 1

**Input:**
`nums = [2,7,11,15], target = 9`
**Output:**
`[0,1]`

### Example 2

**Input:**
`nums = [3,2,4], target = 6`
**Output:**
`[1,2]`

---

## 2) Valid Palindrome

**Topic:** Two Pointers, String
**Difficulty:** Easy

Given a string `s`, determine if it is a palindrome after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

### Example 1

**Input:**
`s = "A man, a plan, a canal: Panama"`
**Output:**
`true`

### Example 2

**Input:**
`s = "race a car"`
**Output:**
`false`

---

## 3) Remove Nth Node From End of List

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium

Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

### Example 1

**Input:**
`head = [1,2,3,4,5], n = 2`
**Output:**
`[1,2,3,5]`

### Example 2

**Input:**
`head = [1], n = 1`
**Output:**
`[]`

---

## 4) Longest Substring Without Repeating Characters

**Topic:** Sliding Window, Hashing
**Difficulty:** Medium

Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1

**Input:**
`s = "abcabcbb"`
**Output:**
`3`
**Explanation:** The answer is `"abc"`.

### Example 2

**Input:**
`s = "bbbbb"`
**Output:**
`1`

---

## 5) Kth Largest Element in an Array

**Topic:** Heaps, Array, Sorting
**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in sorted order, not the `k`th distinct element.

### Example 1

**Input:**
`nums = [3,2,1,5,6,4], k = 2`
**Output:**
`5`

### Example 2

**Input:**
`nums = [3,2,3,1,2,4,5,5,6], k = 4`
**Output:**
`4`

---

## 6) Validate Binary Search Tree

**Topic:** Tree, Binary Tree, BST
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

## 7) Number of Islands

**Topic:** Graphs, Matrices, BFS/DFS
**Difficulty:** Medium

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

### Example 1

**Input:**
`grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]`
**Output:**
`1`

### Example 2

**Input:**
`grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]`
**Output:**
`3`

---

## 8) Daily Temperatures

**Topic:** Stack, Array
**Difficulty:** Medium

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day, keep `answer[i] = 0`.

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

## 9) Design Circular Deque

**Topic:** Queue / Deque, Design
**Difficulty:** Medium

Design your implementation of the circular double-ended queue (deque).

Implement the `MyCircularDeque` class:

* `MyCircularDeque(k)` Initializes the deque with size `k`.
* `insertFront(value)` Inserts an item at the front. Returns `true` if the operation is successful.
* `insertLast(value)` Adds an item at the rear. Returns `true` if the operation is successful.
* `deleteFront()` Deletes an item from the front. Returns `true` if the operation is successful.
* `deleteLast()` Deletes an item from the rear. Returns `true` if the operation is successful.
* `getFront()` Gets the front item. If empty, return `-1`.
* `getRear()` Gets the last item. If empty, return `-1`.
* `isEmpty()` Checks whether the deque is empty.
* `isFull()` Checks whether the deque is full.

### Example

**Input:**
`["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]`
`[[3],[1],[2],[3],[4],[],[],[],[4],[]]`

**Output:**
`[null,true,true,true,false,2,true,true,true,4]`

---

## 10) Median of Two Sorted Arrays

**Topic:** Searching, Binary Search, Arrays
**Difficulty:** Hard

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Example 1

**Input:**
`nums1 = [1,3], nums2 = [2]`
**Output:**
`2.0`

### Example 2

**Input:**
`nums1 = [1,2], nums2 = [3,4]`
**Output:**
`2.5`

---

## Difficulty split

**Easy**

1. Two Sum
2. Valid Palindrome

**Medium**
3. Remove Nth Node From End of List
4. Longest Substring Without Repeating Characters
5. Kth Largest Element in an Array
6. Validate Binary Search Tree
7. Number of Islands
8. Daily Temperatures
9. Design Circular Deque

**Hard**
10. Median of Two Sorted Arrays
