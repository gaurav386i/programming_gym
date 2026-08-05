# Practice Session - 26 May 2026

from collections import deque

from utils import (
    TreeNode, 
    create_bt, 
    ListNode, 
    create_ll,
    print_output,
    print_linked_list,
)

"""
1) Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same.
Two binary trees are considered the same if they are structurally identical, and the nodes 
have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
-----
both input p and q are either valid bts or None.
if any of input is invalid or both are invalid return False
core logic : iterate over both trees and check nodes for equality for both children

"""
def same_bt(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    q = deque([p, q])

    while q:
        n1, n2 = q.popleft()
        if n1 is None and n2 is None:
            continue
        if n1 is None or n2 is None:
            return False

        if n1.key != n2.key:
            return False
        q.append((n1.left, n2.left))
        q.append((n1.right, n2.right))
    
    return True

"""


2) Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

requirements and assumptions: 
input is a valid linkedlist node or None, length of linkedlist is on valid range .
output should be a valid reversed form of input linked list.

core concepts: 
1. create dummy node which will point to head . 
2 . initialise a curr as dummy.next, prev as None and keep 
    reversing until reached the end linked list.

"""


def reverse_ll(head: ListNode) -> ListNode:
    if head is None:
        return head
    dummy = ListNode()
    dummy.next = head
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev


"""


3) Number of Islands
Given an m x n 2D binary grid grid which represents a map 
of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

"""


def dfs(mat: list[list[int]], r: int, c: int) -> None:
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] == "0":
        return 
    # mark visited
    mat[r][c] = "0"
    dfs(mat, r - 1, c)
    dfs(mat, r + 1, c)
    dfs(mat, r, c - 1)
    dfs(mat, r, c + 1)


@print_output
def number_of_islands(mat: list[list[int]]) -> int:
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


"""

4) Jump Game
You are given an integer array nums. You are initially positioned at 
the array's first index, and each element in the array represents your 
maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum 
jump length is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

requirements and assumptions:
i/p is a valid interger list of finite length or None
all elm in list are either +ve int or 0

core logic: 

"""




"""


5) Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.


6) Combination Sum
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen 
numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.
The test cases are generated such that the number of unique combinations 
that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40


7) Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer 
array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the 
same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.


8) Design Twitter
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user, and is able to see the 10 most recent tweets in 
the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID 
  tweetId by the user userId. Each call to this function will be made 
  with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs 
  in the user's news feed. Each item in the news feed must be posted by users 
  who the user followed or by the user themself. Tweets must be ordered from 
  most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started 
  following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started
  unfollowing the user with ID followeeId.

Example 1:
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", 
"unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return [6, 5].
                         // Tweets should be ordered from most recent to least recent.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return [5].

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.


9) Meeting Rooms II
Given an array of meeting time intervals intervals 
where intervals[i] = [starti, endi], return the minimum 
number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6


10) Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner 
being modified to 8. Since there are two 8's in the top left 3x3 sub-box, 
it is invalid.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.
"""

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    number_of_islands(grid)
