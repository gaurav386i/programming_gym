

---

# Set 1

## 1) Same Tree

**Difficulty:** Easy

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Example

**Input:**
`p = [1,2,3], q = [1,2,3]`
**Output:**
`true`

---

## 2) Maximum Depth of Binary Tree

**Difficulty:** Easy

Given the `root` of a binary tree, return its maximum depth.

A binary tree’s maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`3`

---

## 3) Find if Path Exists in Graph

**Difficulty:** Easy

There is a bi-directional graph with `n` vertices. Determine whether there is a valid path from `source` to `destination`.

### Example

**Input:**
`n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2`
**Output:**
`true`

---

## 4) Binary Tree Level Order Traversal

**Difficulty:** Medium

Given the `root` of a binary tree, return the level order traversal of its nodes’ values.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[9,20],[15,7]]`

---

## 5) Number of Islands

**Difficulty:** Medium

Given an `m x n` 2D binary grid `grid` of `'1'`s and `'0'`s, return the number of islands.

### Example

**Input:**
`grid = [["1","1","0"],["1","1","0"],["0","0","1"]]`
**Output:**
`2`

---

## 6) Course Schedule

**Difficulty:** Medium

There are `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`true`

---

## 7) Jump Game

**Difficulty:** Medium

You are given an integer array `nums`. Each element represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Example

**Input:**
`nums = [2,3,1,1,4]`
**Output:**
`true`

---

## 8) Queue Reconstruction by Height

**Difficulty:** Medium

You are given an array `people` where `people[i] = [hi, ki]` represents the `i`th person.

Reconstruct and return the queue.

### Example

**Input:**
`people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
**Output:**
`[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

---

## 9) Validate Binary Search Tree

**Difficulty:** Medium

Given the root of a binary tree, determine if it is a valid binary search tree.

### Example

**Input:**
`root = [2,1,3]`
**Output:**
`true`

---

## 10) Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium

There are some spherical balloons represented as intervals `points`. Return the minimum number of arrows that must be shot to burst all balloons.

### Example

**Input:**
`points = [[10,16],[2,8],[1,6],[7,12]]`
**Output:**
`2`

---

# Set 2

## 1) Invert Binary Tree

**Difficulty:** Easy

Given the `root` of a binary tree, invert the tree, and return its root.

### Example

**Input:**
`root = [4,2,7,1,3,6,9]`
**Output:**
`[4,7,2,9,6,3,1]`

---

## 2) Path Sum

**Difficulty:** Easy

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that the sum of all node values along the path equals `targetSum`.

### Example

**Input:**
`root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
**Output:**
`true`

---

## 3) Flood Fill

**Difficulty:** Easy

An image is represented by an `m x n` integer grid. Perform a flood fill starting from `sr, sc`, changing the starting pixel’s color and all connected pixels of the same color to `color`.

### Example

**Input:**
`image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2`
**Output:**
`[[2,2,2],[2,2,0],[2,0,1]]`

---

## 4) Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes’ values.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`[[3],[20,9],[15,7]]`

---

## 5) Number of Provinces

**Difficulty:** Medium

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` means city `i` and city `j` are directly connected.

Return the number of provinces.

### Example

**Input:**
`isConnected = [[1,1,0],[1,1,0],[0,0,1]]`
**Output:**
`2`

---

## 6) Rotting Oranges

**Difficulty:** Medium

Given an `m x n` grid where each cell can be empty, fresh, or rotten, return the minimum number of minutes needed until no fresh orange remains. If impossible, return `-1`.

### Example

**Input:**
`grid = [[2,1,1],[1,1,0],[0,1,1]]`
**Output:**
`4`

---

## 7) Jump Game II

**Difficulty:** Medium

You are given an array `nums`. Each element represents your maximum jump length at that position.

Return the minimum number of jumps needed to reach the last index.

### Example

**Input:**
`nums = [2,3,1,1,4]`
**Output:**
`2`

---

## 8) Non-overlapping Intervals

**Difficulty:** Medium

Given an array of intervals, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Example

**Input:**
`intervals = [[1,2],[2,3],[3,4],[1,3]]`
**Output:**
`1`

---

## 9) Kth Smallest Element in a BST

**Difficulty:** Medium

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value of all values of the nodes in the tree.

### Example

**Input:**
`root = [3,1,4,null,2], k = 1`
**Output:**
`1`

---

## 10) Is Graph Bipartite?

**Difficulty:** Medium

Given an undirected graph, return `true` if and only if it is bipartite.

### Example

**Input:**
`graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`
**Output:**
`false`

---

# Set 3

## 1) Symmetric Tree

**Difficulty:** Easy

Given the `root` of a binary tree, check whether it is a mirror of itself.

### Example

**Input:**
`root = [1,2,2,3,4,4,3]`
**Output:**
`true`

---

## 2) Balanced Binary Tree

**Difficulty:** Easy

Given a binary tree, determine if it is height-balanced.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`true`

---

## 3) Search in a Binary Search Tree

**Difficulty:** Easy

Given the root of a binary search tree and an integer `val`, return the subtree rooted with the node whose value equals `val`. If such a node does not exist, return `null`.

### Example

**Input:**
`root = [4,2,7,1,3], val = 2`
**Output:**
`[2,1,3]`

---

## 4) Binary Tree Right Side View

**Difficulty:** Medium

Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking from the right side.

### Example

**Input:**
`root = [1,2,3,null,5,null,4]`
**Output:**
`[1,3,4]`

---

## 5) Clone Graph

**Difficulty:** Medium

Given a reference of a node in a connected undirected graph, return a deep copy of the graph.

### Example

**Input:**
`adjList = [[2,4],[1,3],[2,4],[1,3]]`
**Output:**
`[[2,4],[1,3],[2,4],[1,3]]`

---

## 6) Course Schedule II

**Difficulty:** Medium

There are `numCourses` courses you have to take. Return the ordering of courses you should take to finish all courses. If impossible, return an empty array.

### Example

**Input:**
`numCourses = 2, prerequisites = [[1,0]]`
**Output:**
`[0,1]`

---

## 7) Gas Station

**Difficulty:** Medium

There are `n` gas stations along a circular route. Return the starting gas station’s index if you can travel around the circuit once, otherwise return `-1`.

### Example

**Input:**
`gas = [1,2,3,4,5], cost = [3,4,5,1,2]`
**Output:**
`3`

---

## 8) Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium

Given a binary tree, find the lowest common ancestor of two given nodes in the tree.

### Example

**Input:**
`root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
**Output:**
`3`

---

## 9) Surrounded Regions

**Difficulty:** Medium

Given an `m x n` board containing `'X'` and `'O'`, capture all regions surrounded by `'X'`.

### Example

**Input:**
`board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
**Output:**
`[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

---

## 10) 01 Matrix

**Difficulty:** Medium

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

### Example

**Input:**
`mat = [[0,0,0],[0,1,0],[1,1,1]]`
**Output:**
`[[0,0,0],[0,1,0],[1,2,1]]`

---

# Set 4

## 1) N-ary Tree Preorder Traversal

**Difficulty:** Easy

Given the `root` of an n-ary tree, return the preorder traversal of its nodes’ values.

### Example

**Input:**
`root = [1,null,3,2,4,null,5,6]`
**Output:**
`[1,3,5,6,2,4]`

---

## 2) Binary Tree Paths

**Difficulty:** Easy

Given the `root` of a binary tree, return all root-to-leaf paths in any order.

### Example

**Input:**
`root = [1,2,3,null,5]`
**Output:**
`["1->2->5","1->3"]`

---

## 3) Find Center of Star Graph

**Difficulty:** Easy

There is an undirected star graph consisting of `n` nodes labeled from `1` to `n`. You are given a 2D array `edges` where each edge connects the center with another node.

Return the center of the star graph.

### Example

**Input:**
`edges = [[1,2],[2,3],[4,2]]`
**Output:**
`2`

---

## 4) Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium

Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.

### Example

**Input:**
`preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]`
**Output:**
`[3,9,20,null,null,15,7]`

---

## 5) Max Area of Island

**Difficulty:** Medium

Given a binary matrix `grid`, return the maximum area of an island.

### Example

**Input:**
`grid = [[0,0,1,0],[1,1,1,0],[0,1,0,0]]`
**Output:**
`5`

---

## 6) Pacific Atlantic Water Flow

**Difficulty:** Medium

Given an `m x n` matrix of heights, return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

### Example

**Input:**
`heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
**Output:**
`[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

---

## 7) Open the Lock

**Difficulty:** Medium

You have a lock in front of you with 4 circular wheels. Return the minimum total number of turns required to open the lock, or `-1` if impossible.

### Example

**Input:**
`deadends = ["0201","0101","0102","1212","2002"], target = "0202"`
**Output:**
`6`

---

## 8) Sum Root to Leaf Numbers

**Difficulty:** Medium

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path represents a number.

Return the total sum of all root-to-leaf numbers.

### Example

**Input:**
`root = [1,2,3]`
**Output:**
`25`

---

## 9) Populating Next Right Pointers in Each Node II

**Difficulty:** Medium

Given a binary tree, populate each `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.

### Example

**Input:**
`root = [1,2,3,4,5,null,7]`
**Output:**
`[1,#,2,3,#,4,5,7,#]`

---

## 10) Redundant Connection

**Difficulty:** Medium

In a graph that started as a tree with one additional edge added, return an edge that can be removed so that the resulting graph is a tree.

### Example

**Input:**
`edges = [[1,2],[1,3],[2,3]]`
**Output:**
`[2,3]`

---

# Set 5

## 1) N-ary Tree Postorder Traversal

**Difficulty:** Easy

Given the `root` of an n-ary tree, return the postorder traversal of its nodes’ values.

### Example

**Input:**
`root = [1,null,3,2,4,null,5,6]`
**Output:**
`[5,6,3,2,4,1]`

---

## 2) Minimum Depth of Binary Tree

**Difficulty:** Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

### Example

**Input:**
`root = [3,9,20,null,null,15,7]`
**Output:**
`2`

---

## 3) Employee Importance

**Difficulty:** Easy

You have a data structure of employee information, including the employee's unique id, importance value, and direct subordinates' ids.

Given the employee list and an employee id, return the total importance value of this employee and all their subordinates.

### Example

**Input:**
`employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1`
**Output:**
`11`

---

## 4) Flatten Binary Tree to Linked List

**Difficulty:** Medium

Given the `root` of a binary tree, flatten it into a linked list in-place following preorder traversal.

### Example

**Input:**
`root = [1,2,5,3,4,null,6]`
**Output:**
`[1,null,2,null,3,null,4,null,5,null,6]`

---

## 5) House Robber III

**Difficulty:** Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house.

After a robbery, the police will be alerted automatically if two directly-linked houses were broken into on the same night.

Return the maximum amount of money the thief can rob without alerting the police.

### Example

**Input:**
`root = [3,2,3,null,3,null,1]`
**Output:**
`7`

---

## 6) Count Good Nodes in Binary Tree

**Difficulty:** Medium

Given a binary tree root, a node `X` in the tree is named good if on the path from root to `X` there are no nodes with a value greater than `X`.

Return the number of good nodes in the binary tree.

### Example

**Input:**
`root = [3,1,4,3,null,1,5]`
**Output:**
`4`

---

## 7) Path Sum II

**Difficulty:** Medium

Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values equals `targetSum`.

### Example

**Input:**
`root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22`
**Output:**
`[[5,4,11,2],[5,8,4,5]]`

---

## 8) All Paths From Source to Target

**Difficulty:** Medium

Given a directed acyclic graph of `n` nodes, find all possible paths from node `0` to node `n - 1`.

### Example

**Input:**
`graph = [[1,2],[3],[3],[]]`
**Output:**
`[[0,1,3],[0,2,3]]`

---

## 9) Evaluate Division

**Difficulty:** Medium

You are given an array of variable pairs `equations` and an array of real numbers `values`, where each pair represents an equation and each value represents the answer to that equation.

Return the answers to all queries.

### Example

**Input:**
`equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"]]`
**Output:**
`[6.0,0.5,-1.0]`

---

## 10) Task Scheduler

**Difficulty:** Medium

You are given an array of CPU tasks and a non-negative cooling time `n`.

Return the minimum number of intervals the CPU will take to finish all the tasks.

### Example

**Input:**
`tasks = ["A","A","A","B","B","B"], n = 2`
**Output:**
`8`

