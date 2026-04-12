
---

## 1) Contains Duplicate

**Topic:** Array, Hashing
**Difficulty:** Easy
**Suggested time limit:** 8 minutes

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1

**Input:**
`nums = [1,2,3,1]`
**Output:**
`true`

### Example 2

**Input:**
`nums = [1,2,3,4]`
**Output:**
`false`

### Constraints

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## 2) Same Tree

**Topic:** Tree, Binary Tree
**Difficulty:** Easy
**Suggested time limit:** 10 minutes

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

### Example 1

**Input:**
`p = [1,2,3], q = [1,2,3]`
**Output:**
`true`

### Example 2

**Input:**
`p = [1,2], q = [1,null,2]`
**Output:**
`false`

### Constraints

* The number of nodes in both trees is in the range `[0, 100]`
* `-10^4 <= Node.val <= 10^4`

---

## 3) Product of Array Except Self

**Topic:** Array
**Difficulty:** Medium
**Suggested time limit:** 18 minutes

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in `O(n)` time and without using division.

### Example 1

**Input:**
`nums = [1,2,3,4]`
**Output:**
`[24,12,8,6]`

### Example 2

**Input:**
`nums = [-1,1,0,-3,3]`
**Output:**
`[0,0,9,0,0]`

### Constraints

* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`

---

## 4) Sort Colors

**Topic:** Two Pointers, Sorting, Array
**Difficulty:** Medium
**Suggested time limit:** 15 minutes

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Use the integers `0`, `1`, and `2` to represent the color red, white, and blue respectively.

You must solve this problem without using the library’s sort function.

### Example 1

**Input:**
`nums = [2,0,2,1,1,0]`
**Output:**
`[0,0,1,1,2,2]`

### Example 2

**Input:**
`nums = [2,0,1]`
**Output:**
`[0,1,2]`

### Constraints

* `1 <= nums.length <= 300`
* `nums[i] is either 0, 1, or 2`

---

## 5) Linked List Cycle II

**Topic:** Linked List, Slow and Fast Pointers
**Difficulty:** Medium
**Suggested time limit:** 20 minutes

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

Do not modify the linked list.

### Example 1

**Input:**
`head = [3,2,0,-4], pos = 1`
**Output:**
`tail connects to node index 1`

### Example 2

**Input:**
`head = [1,2], pos = 0`
**Output:**
`tail connects to node index 0`

### Example 3

**Input:**
`head = [1], pos = -1`
**Output:**
`no cycle`

### Constraints

* The number of nodes in the list is in the range `[0, 10^4]`
* `-10^5 <= Node.val <= 10^5`

---

## 6) Permutation in String

**Topic:** Sliding Window, Hashing
**Difficulty:** Medium
**Suggested time limit:** 20 minutes

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Example 1

**Input:**
`s1 = "ab", s2 = "eidbaooo"`
**Output:**
`true`

### Example 2

**Input:**
`s1 = "ab", s2 = "eidboaoo"`
**Output:**
`false`

### Constraints

* `1 <= s1.length, s2.length <= 10^4`
* `s1` and `s2` consist of lowercase English letters

---

## 7) K Closest Points to Origin

**Topic:** Heaps, Array
**Difficulty:** Medium
**Suggested time limit:** 18 minutes

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points is the Euclidean distance.

You may return the answer in any order.

### Example 1

**Input:**
`points = [[1,3],[-2,2]], k = 1`
**Output:**
`[[-2,2]]`

### Example 2

**Input:**
`points = [[3,3],[5,-1],[-2,4]], k = 2`
**Output:**
`[[3,3],[-2,4]]`

### Constraints

* `1 <= k <= points.length <= 10^4`
* `-10^4 <= xi, yi <= 10^4`

---

## 8) Binary Tree Level Order Traversal

**Topic:** Tree, Queue / Deque, BFS
**Difficulty:** Medium
**Suggested time limit:** 18 minutes

Given the root of a binary tree, return the level order traversal of its nodes’ values.
That is, from left to right, level by level.

### Example 1

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[9,20],[15,7]]`

### Example 2

**Input:**
`root = [1]`
**Output:**
`[[1]]`

### Example 3

**Input:**
`root = []`
**Output:**
`[]`

### Constraints

* The number of nodes in the tree is in the range `[0, 2000]`
* `-1000 <= Node.val <= 1000`

---

## 9) Search a 2D Matrix

**Topic:** Searching, Binary Search, Matrices
**Difficulty:** Medium
**Suggested time limit:** 15 minutes

You are given an `m x n` integer matrix `matrix` with the following two properties:

* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false` otherwise.

### Example 1

**Input:**
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3`
**Output:**
`true`

### Example 2

**Input:**
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13`
**Output:**
`false`

### Constraints

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-10^4 <= matrix[i][j], target <= 10^4`

---

## 10) Merge k Sorted Lists

**Topic:** Linked List, Heaps
**Difficulty:** Hard
**Suggested time limit:** 30 minutes

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Example 1

**Input:**
`lists = [[1,4,5],[1,3,4],[2,6]]`
**Output:**
`[1,1,2,3,4,4,5,6]`

### Example 2

**Input:**
`lists = []`
**Output:**
`[]`

### Example 3

**Input:**
`lists = [[]]`
**Output:**
`[]`

### Constraints

* `k == lists.length`
* `0 <= k <= 10^4`
* `0 <= lists[i].length <= 500`
* `-10^4 <= lists[i][j] <= 10^4`
* `lists[i]` is sorted in ascending order

---

# Difficulty split

## Easy

1. Contains Duplicate
2. Same Tree

## Medium

3. Product of Array Except Self
4. Sort Colors
5. Linked List Cycle II
6. Permutation in String
7. K Closest Points to Origin
8. Binary Tree Level Order Traversal
9. Search a 2D Matrix

## Hard

10. Merge k Sorted Lists

# Suggested mock timing

* **Easy:** 8 to 10 minutes each
* **Medium:** 15 to 20 minutes each
* **Hard:** 30 minutes

