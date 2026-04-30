
---

# Set 1

## 1) Two Sum

**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use the same element twice.

### Example

**Input:**
`nums = [2,7,11,15], target = 9`
**Output:**
`[0,1]`

---

## 2) Same Tree

**Difficulty:** Easy

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

### Example

**Input:**
`p = [1,2,3], q = [1,2,3]`
**Output:**
`true`

---

## 3) Best Time to Buy and Sell Stock

**Difficulty:** Easy

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock.

Return the maximum profit you can achieve.

### Example

**Input:**
`prices = [7,1,5,3,6,4]`
**Output:**
`5`

---

## 4) Longest Substring Without Repeating Characters

**Difficulty:** Medium

Given a string `s`, find the length of the longest substring without repeating characters.

### Example

**Input:**
`s = "abcabcbb"`
**Output:**
`3`

---

## 5) Number of Islands

**Difficulty:** Medium

Given an `m x n` grid of `'1'`s and `'0'`s, return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

### Example

**Input:**
`grid = [["1","1","0"],["1","1","0"],["0","0","1"]]`
**Output:**
`2`

---

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
`["MyCircularDeque","insertLast","insertLast","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]`
`[[3],[1],[2],[3],[],[],[],[4],[]]`

**Output:**
`[null,true,true,true,2,true,true,true,4]`

---

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

## 8) Merge Intervals

**Difficulty:** Medium

Given an array of intervals `intervals`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example

**Input:**
`intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:**
`[[1,6],[8,10],[15,18]]`

---

## 9) Maximum Sum Subarray of Size K

**Difficulty:** Medium

Given an array of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.

### Example

**Input:**
`nums = [2,1,5,1,3,2], k = 3`
**Output:**
`9`

---

## 10) Group Anagrams

**Difficulty:** Medium

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Example

**Input:**
`strs = ["eat","tea","tan","ate","nat","bat"]`
**Output:**
`[["bat"],["nat","tan"],["ate","eat","tea"]]`

---

# Set 2

## 1) Valid Palindrome

**Difficulty:** Easy

Given a string `s`, determine if it is a palindrome after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

### Example

**Input:**
`s = "A man, a plan, a canal: Panama"`
**Output:**
`true`

---

## 2) Remove Duplicates from Sorted Array

**Difficulty:** Easy

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

Return the number of unique elements.

### Example

**Input:**
`nums = [1,1,2]`
**Output:**
`2`

---

## 3) Search in a Binary Search Tree

**Difficulty:** Easy

You are given the root of a binary search tree and an integer `val`.

Find the node in the BST whose value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

### Example

**Input:**
`root = [4,2,7,1,3], val = 2`
**Output:**
`[2,1,3]`

---

## 4) Spiral Matrix

**Difficulty:** Medium

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Example

**Input:**
`matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:**
`[1,2,3,6,9,8,7,4,5]`

---

## 5) Container With Most Water

**Difficulty:** Medium

You are given an integer array `height`. Find two lines that together with the x-axis form a container that holds the most water.

Return the maximum amount of water a container can store.

### Example

**Input:**
`height = [1,8,6,2,5,4,8,3,7]`
**Output:**
`49`

---

## 6) Search Insert Position

**Difficulty:** Medium

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If not, return the index where it would be inserted in order.

### Example

**Input:**
`nums = [1,3,5,6], target = 5`
**Output:**
`2`

---

## 7) Find Peak Element

**Difficulty:** Medium

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of them.

### Example

**Input:**
`nums = [1,2,3,1]`
**Output:**
`2`

---

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

## 9) Palindrome Linked List

**Difficulty:** Medium

Given the head of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

### Example

**Input:**
`head = [1,2,2,1]`
**Output:**
`true`

---

## 10) Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes’ values.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[20,9],[15,7]]`

---

# Set 3

## 1) Contains Duplicate

**Difficulty:** Easy

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example

**Input:**
`nums = [1,2,3,1]`
**Output:**
`true`

---

## 2) Invert Binary Tree

**Difficulty:** Easy

Given the root of a binary tree, invert the tree, and return its root.

### Example

**Input:**
`root = [4,2,7,1,3,6,9]`
**Output:**
`[4,7,2,9,6,3,1]`

---

## 3) Middle of the Linked List

**Difficulty:** Easy

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

### Example

**Input:**
`head = [1,2,3,4,5,6]`
**Output:**
`[4,5,6]`

---

## 4) Find All Duplicates in an Array

**Difficulty:** Medium

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appears twice.

### Example

**Input:**
`nums = [4,3,2,7,8,2,3,1]`
**Output:**
`[2,3]`

---

## 5) Course Schedule II

**Difficulty:** Medium

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

### Example

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`[0,1]`

---

## 6) Sort List

**Difficulty:** Medium

Given the head of a linked list, return the list after sorting it in ascending order.

### Example

**Input:**
`head = [4,2,1,3]`
**Output:**
`[1,2,3,4]`

---

## 7) Koko Eating Bananas

**Difficulty:** Medium

Given an array `piles` where `piles[i]` represents the number of bananas in the `i`th pile, and an integer `h`, return the minimum integer `k` such that Koko can eat all bananas within `h` hours.

### Example

**Input:**
`piles = [3,6,7,11], h = 8`
**Output:**
`4`

---

## 8) Binary Tree Right Side View

**Difficulty:** Medium

Given the root of a binary tree, imagine yourself standing on the right side of it.

Return the values of the nodes you can see ordered from top to bottom.

### Example

**Input:**
`root = [1,2,3,null,5,null,4]`
**Output:**
`[1,3,4]`

---

## 9) Reorganize String

**Difficulty:** Medium

Given a string `s`, rearrange the characters so that no two adjacent characters are the same.

Return any possible rearrangement or return an empty string if not possible.

### Example

**Input:**
`s = "aab"`
**Output:**
`"aba"`

---

## 10) K Closest Points to Origin

**Difficulty:** Medium

Given an array of points where `points[i] = [xi, yi]` and an integer `k`, return the `k` closest points to the origin.

### Example

**Input:**
`points = [[1,3],[-2,2]], k = 1`
**Output:**
`[[-2,2]]`

---

# Set 4

## 1) Backspace String Compare

**Difficulty:** Easy

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

### Example

**Input:**
`s = "ab#c", t = "ad#c"`
**Output:**
`true`

---

## 2) Find the Difference

**Difficulty:** Easy

You are given two strings `s` and `t`.

String `t` is generated by random shuffling string `s` and then adding one more letter at a random position.

Return the letter that was added to `t`.

### Example

**Input:**
`s = "abcd", t = "abcde"`
**Output:**
`"e"`

---

## 3) Implement Queue using Stacks

**Difficulty:** Easy

Implement a first in first out (FIFO) queue using only two stacks.

Implement the `MyQueue` class:

* `push(x)`
* `pop()`
* `peek()`
* `empty()`

### Example

**Input:**
`["MyQueue","push","push","peek","pop","empty"]`
`[[],[1],[2],[],[],[]]`

**Output:**
`[null,null,null,1,1,false]`

---

## 4) Sort Characters By Frequency

**Difficulty:** Medium

Given a string `s`, sort it in decreasing order based on the frequency of the characters.

### Example

**Input:**
`s = "tree"`
**Output:**
`"eert"`

---

## 5) Find All Anagrams in a String

**Difficulty:** Medium

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

### Example

**Input:**
`s = "cbaebabacd", p = "abc"`
**Output:**
`[0,6]`

---

## 6) Trapping Rain Water

**Difficulty:** Medium

Given `n` non-negative integers representing an elevation map, compute how much water it can trap after raining.

### Example

**Input:**
`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
**Output:**
`6`

---

## 7) Find the Duplicate Number

**Difficulty:** Medium

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`, return the duplicate number.

You must solve the problem without modifying the array and using only constant extra space.

### Example

**Input:**
`nums = [1,3,4,2,2]`
**Output:**
`2`

---

## 8) Remove Duplicates from Sorted List II

**Difficulty:** Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

### Example

**Input:**
`head = [1,2,3,3,4,4,5]`
**Output:**
`[1,2,5]`

---

## 9) Partition List

**Difficulty:** Medium

Given the head of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

### Example

**Input:**
`head = [1,4,3,2,5,2], x = 3`
**Output:**
`[1,2,2,4,3,5]`

---

## 10) Queue Reconstruction by Height

**Difficulty:** Medium

You are given an array of people `people` where `people[i] = [hi, ki]` represents the `i`th person.

Reconstruct and return the queue.

### Example

**Input:**
`people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
**Output:**
`[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

---

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

## 4) Remove Duplicates from Sorted Array II

**Difficulty:** Medium

Given an integer array `nums` sorted in non-decreasing order, remove duplicates in-place such that each unique element appears at most twice.

Return the new length.

### Example

**Input:**
`nums = [1,1,1,2,2,3]`
**Output:**
`5`

---

## 5) Reverse Linked List in Pairs

**Difficulty:** Medium

Given the head of a linked list, swap every two adjacent nodes and return the head of the modified list.

### Example

**Input:**
`head = [1,2,3,4]`
**Output:**
`[2,1,4,3]`

---

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

## 7) Validate Binary Search Tree

**Difficulty:** Medium

Given the root of a binary tree, determine whether it is a valid binary search tree.

### Example

**Input:**
`root = [5,1,4,null,null,3,6]`
**Output:**
`false`

---

## 8) Daily Temperatures

**Difficulty:** Medium

Given an array of daily temperatures, return an array such that `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature.

### Example

**Input:**
`temperatures = [73,74,75,71,69,72,76,73]`
**Output:**
`[1,1,4,2,1,1,0,0]`

---

## 9) Find K Pairs with Smallest Sums

**Difficulty:** Medium

You are given two sorted arrays `nums1` and `nums2` and an integer `k`.

Return the `k` pairs with the smallest sums.

### Example

**Input:**
`nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
**Output:**
`[[1,2],[1,4],[1,6]]`

---

## 10) Add Two Numbers

**Difficulty:** Medium

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

**Input:**
`l1 = [2,4,3], l2 = [5,6,4]`
**Output:**
`[7,0,8]`

---

