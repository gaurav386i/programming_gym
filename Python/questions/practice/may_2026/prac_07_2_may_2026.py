from collections import deque

from utils import (
    print_output, 
    TreeNode, 
    create_bt, 
    tree_to_list,
    ListNode,
    create_ll,
    print_linked_list,
)

"""

1) Intersection of Two Arrays II
  Topic: Array, Hashing, Two Pointers, Sorting
  Difficulty: Easy

  Given two integer arrays nums1 and nums2, return an array 
  of their intersection. Each element in the result must appear 
  as many times as it shows in both
  arrays and you may return the result in any order.

  Example
  Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  Output: [4,9] (or [9,4])

---
constraints:
What will be exception scenario :
    1. what is nums1 or nums2 is not provided 
    2. what will be size of both arr is always unequal 
       or can be equal , can nums2 can be smaller and nums1
       can be bigger.
    3. Output can in any order ?

logic to solve the problem:
naive approach
 for each element in nums1:
     will iterate nums2 and check if, found a match add 
     that response list, do until all elements of nums1 
     are exhausted 
optimised approach
    1. create a set of smaller list .
    2. sort bigger list and iterate through it 
       and check if elm in set if yes then move add it 
       response and move forward:

"""

def get_freq(seq: str | list) -> dict[str | int, int]:
    freq = {}
    if not seq:
        return freq
    for w in seq:
        freq[w] = freq.get(w, 0) + 1
    return freq


@print_output
def intersection_of_two_arr(
    nums1: list[int], nums2: list[int]
) -> list[int]:
    resp = []
    if not nums1 or not nums2:
        return resp
    
    f_nums1 = get_freq(nums1)
    for n in nums2:
        if f_nums1.get(n, 0) > 0:
            resp.append(n)
            f_nums1[n] -= 1
    return resp
            
    
    

def intersection_of_two_arr_2(
        nums1: list[int], nums2: list[int]
):
    nums1.sort()
    nums2.sort()
    p1, p2 = 0, 0
    res = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
          
    return res

        


"""

  2) Merge Two Binary Trees
  Topic: Binary Tree, Recursion
  Difficulty: Easy

  You are given two binary trees root1 and root2. 
  Imagine that when you put one of them to cover the other, 
  some nodes of the two trees are overlapped while
  the others are not. You need to merge the two trees 
  into a new binary tree. The merge rule is that if 
  two nodes overlap, then sum node values up as the new
  value of the merged node. Otherwise, the NOT null node 
  will be used as the node of the new tree.

  Example
  Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
  Output: [3,4,5,5,4,null,7]

  ---
  assumptions, constraints and exceptions :
  1. Are both input always present or we need to handle if on is 
     not given or both is not given .
  2. Is there is constraints on size of both trees or it could be anything like 
     r1 < r2, r1 > r2 or r1 == r2 .
  3. I assume node values/keys are always int , new node will be sum of two , it will one 
     which is not None , what if both node are node . 
naive approach :
   Create root node by adding roots of both inputs tree and in a if/else branch
   and then recursively call with left and right childs.

efficient approach : 
  Initialise a stack like st = [(r1, r2)], pop it create new node, and append
  stack again with new node and r1.left, r2.left and r1.right, r2.right and and keep adding 
  left and right child until stack is not empty 
"""

def merge_bt(r1: TreeNode, r2: TreeNode) -> TreeNode | None:

    if not r1 and not r2:
        return None
    val = (r1.key if r1 else 0) + (r2.key if r2 else 0)
    new_root = TreeNode(val)
    
    new_root.leff = merge_bt(
        r1.left if r1 else None,
        r2.left if r2 else None
    )
    new_root.right = merge_bt(
        r1.right if r1 else None,
        r2.right if r2 else None
    )

    return new_root

def inplace_merge(r1: TreeNode, r2: TreeNode) -> TreeNode | None:
    if not r1 and not r2:
        return None
    r1.key += r2.key
    r1.left = merge_bt(
        r1.left if r1 else None,
        r2.left if r2 else None
    )
    r1.right = merge_bt(
        r1.right if r2 else None,
        r2.left if r2 else None
    )
    return  r1


def merge_bts_itr(r1: TreeNode, r2: TreeNode) -> TreeNode | None:
    if not r1 and not r2:
        return None
    st = [(r1, r2)]
    while st:
        n1, n2 = st.pop()

        n1.key += n2.key

        if n1.left and n2.left:
            st.append((n1.left, n2.left))
        elif n2.left:
            n1.left = n2.left
        
        if n1.right and n2.right:
            st.append((n1.right, n2.right))
        elif n2.right:
            n1.right = n2.right
    return r1




"""

  3) Rotate List
  Topic: Linked List, Two Pointers
  Difficulty: Medium

  Given the head of a linked list, rotate the list 
  to the right by k places.

  Example
  Input: head = [1,2,3,4,5], k = 2
  Output: [4,5,1,2,3]

  ---
constraints, assumptions and exceptions:
# how to handle if input is None, 
# what to return if value of k is more than length of linkedlist
assunptions:
# input will be always a object of ll Node or None
# Rotation is always to right 
# k will be always less than length of list

naive approach : iterate the whole list and calculate length of list, detach 
                 last node point it to head and make new node and iterate again 
                 and do this for k times 

efficeint approach: 
start with two pointers first > > head and seceond >> head + k
iterate both and reach the end of list and then detach list from first and 
point second to the head of list and return second 

"""

def rotate_ll_right_by_k(head: ListNode, k: int) -> ListNode | None:
    if not head:
        return None
    first = head
    second = head

    for _ in range(k):
        second = second.next
    while second and second.next:
        first = first.next
        second = second.next
    rotate_head = first.next
    second.next = head
    first.next = None
    return rotate_head
    
# time complexity O(n + k) > O(n)
# space O(1) 

"""


  4) Permutation in String
  Topic: Sliding Window, Hashing, String
  Difficulty: Medium

  Given two strings s1 and s2, return true if s2 contains a 
  permutation of s1, or false otherwise. In other words, return 
  true if one of s1's permutations is
  the substring of s2.

  Example
  Input: s1 = "ab", s2 = "eidbaooo"
  Output: true (Explanation: s2 contains one permutation of s1 ("ba")).

---
# constraints, assumptions and exceptions: 
# how to handle if both or one of inputs are not provided , what if length of s1 is greater
  than length of s2 , do string always contains alphabets or other asci chars can be there 

# assumptions:
# inputs are always string of alphanumeric chars , input are always object of string 

naive approach: create all possible permutation of s1 and iterate s2 and check if that
                that string present in s2 of length equals to s1 
                TC >> O(n2) and space we are storing test string in constant space so O(1)

efficent approach : create a frequency map of chars in s1 and slide a window on s2 and calucating 
                    char freq and equating it with s1 freq return if found or return false                

"""


@print_output
def permutation_of_s1_in_s2(s1: str, s2: str) -> bool:
    if not s1 or not s2 or len(s1) > len(s2):
        return False
    s1_freq = get_freq(s1)
    left = 0
    for right in range(len(s1) - 1, len(s2)):
        if s1_freq == get_freq(s2[left:right + 1]):
            return True
        left += 1
    return False


"""

  5) Find First and Last Position of Element in Sorted Array
  Topic: Binary Search, Array
  Difficulty: Medium

  Given an array of integers nums sorted in non-decreasing order, 
  find the starting and ending position of a given target value. If target is not found in the
  array, return [-1, -1]. You must write an algorithm with (log n) runtime complexity.

  Example
  Input: nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]

---
# constraints, assumptions and exception handling 
# how to handle if array is None or empty , how to handle if target itself is not given 
# assumptions : 
              it is always an arr of int , with finite length 
              as problem ask to do it in log n time we have to user binary search 
              as it is sorted array so elements are ajdacent to each other 
naive approach: do binary search and return item and item + 1

efficient approach : 
             write two methods that will find first and last elements using binary search and if you found 
             first element keep going left and last if found element keep going right found last element 

"""

@print_output
def find_first_and_last(nums: list[int], target: int) -> list[int]:
    # [5,7,7,8,8,10]
    if not nums or not target:
        return [-1, -1]
    def find_first():
        left = 0
        right = len(nums) - 1
        first =  -1 
        while left <= right:
          mid = (right + left) // 2
          if nums[mid] == target:
              first = mid
              right = mid - 1
          elif nums[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
        return first
    def find_last():
        left = 0
        right = len(nums) - 1
        last = -1 
        while left <= right:
          mid = (right + left ) // 2
          if nums[mid] == target:
              last = mid
              left = mid + 1
          elif nums[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
        return last
    return [find_first(), find_last()]
        

"""


  6) N-ary Tree Level Order Traversal
  Topic: N-ary Tree, BFS, Queue
  Difficulty: Medium

  Given an n-ary tree, return the level order traversal of its 
  nodes' values. (i.e., from left to right, level by level).

  Example
  Input: root = [1,null,3,2,4,null,5,6]
  Output: [[1],[3,2,4],[5,6]]

  ---
# constraints, assumptions , exceptions 
# contraints : how to handle if input is not provided or None, 
# assumptions : input will be a valid N-ary tree or None of 
#               finite height and width
#               output will be a list of level 
# naive approach is to iterate to each level in recurive manner and store key in list
# 
# efficent approach : Will be lavel order traversal using queue 
"""

class _Node:
    def __init__(self, key: int, children: list["_Node"] | None = None):
        self.key = key
        self.children = children if children is not None else []

def n_ary_level_order_traversal(root: _Node) -> list[list[int]]:
    if root is None:
        return []
    q = deque([root])
    result = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
          node = q.popleft()
          level.append(node.key)

            
          for child in node.children:
            q.append(child)
        result.append(level)
    return result        

"""

  7) Decode String
  Topic: Stack, Recursion, String
  Difficulty: Medium

  Given an encoded string, return its decoded string. 
  The encoding rule is: k[encoded_string], where the encoded_string 
  inside the square brackets is being
  repeated exactly k times. Note that k is guaranteed to be a positive integer.

  Example
  Input: s = "3[a2[c]]"
  Output: "accaccacc"
  
  # constraints, assumptions and exceptions handling 
    how to handle if input is not provided 

# constraints , assumptions and error handling :
1. how to handle if input is None , 
# assumptions : input length is finite , input is str which contains either alphanumeric char and []
#              : k is positive and brackets are always open and close no invalid brackets 
naive approach : not able to get 
efficient approach: push all elm of string in stack , once done pop element , store k in num and store ch 
in temp container and keep adding element until we get closing sq bracket once got it multiple k into string 
created from collected chars. continue 
  ---
"""


@print_output
def decode_encoded_word(s: str) -> str:
    if not s:
        return ""
    
    st = []
    curr_num = 0
    curr_str = ""
    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            st.append((curr_str, curr_num))
            curr_num = 0
            curr_str = ""
        elif ch == "]":
            prev_str, prev_num = st.pop()
            curr_str = prev_str + curr_str * prev_num
        else:
            curr_str += ch

    return curr_str



"""

  8) Partition Labels
  Topic: Greedy, Hashing, Two Pointers
  Difficulty: Medium

  You are given a string s. We want to partition the string into as 
  many parts as possible so that each letter appears in at most one 
  part. Return a list of
  integers representing the size of these parts.

  Example
  Input: s = "ababcbacadefegdehijhklij"
  Output: [9,7,8] (Explanation: The partitions are "ababcbaca", "defegde", "hijhklij".)

  ---
# contaraints: how to handle if input is not provided, what if input got numbers and other asci chars 
               what will be size of input, Is there a case where string contains only one 
               chars or one char multiple times
 assumption : Input is an string , of alphabilical chars of finite length , output will integers of len if each 
              subsrtring, string may contains same or different chars 

Naive logic : Create a frequency map of string and iterate through string and keep decreasing count if freq > 0 if 
              encounter for a char or a group of char become zero store length of that substring in result, 
              keep tracking group of chars and keep updating max index of these char add to the result whose index, 
              is max when it count became zero . or we can run two pointer to keep checking first and last appearance 
              of a char but I am thinking how to know how many char to track 

"""


@print_output
def partion_labels(s: str) -> list[int]:
    if not s:
        return []
    last = {ch: i for i, ch in enumerate(s)}
    start = end = 0
    result = []
    for i, ch in enumerate(s):
        end = max(end, last[ch])

        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result


"""

  9) Word Search
  Topic: Matrix, Backtracking, DFS
  Difficulty: Medium

  Given an m x n grid of characters board and a string word, return true if word 
  exists in the grid. The word can be constructed from letters of sequentially
  adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
  The same letter cell may not be used more than once.

  Example
  Input: board = [
          ["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]
        ], word = "ABCCED"
  Output: true

constraints: 
           how to handle if input is not given , given but first column itself is None or empty. Is it going to
           be a square matrix, what it means by sequential adjacent cells 
assumptions : input is a m x n matrix , all elem are english, capital alphabets, both m and n are of finite
              length . Words contructed using 
core logic :
           updated logic 
---
"""


def dfs(mat: list[list[str]], r: int, c: int, i: int, word: str) -> None:
    if i == len(word):
        return True
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] != word[i]:
        return False
    temp = mat[r][c]
    mat[r][c] = "#"
    found = (
        dfs(mat, r + 1, c , i + 1, word) or
        dfs(mat, r -1 , c , i + 1, word) or
        dfs(mat, r, c + 1, i + 1, word) or
        dfs(mat, r, c - 1 , i + 1, word)
    )
    mat[r][c] = temp
    return found
    
    

@print_output
def search_word_in_matrix(mat: list[list[str]], word: str) -> bool:
    if not mat or not mat[0]:
        return False
    rows = len(mat)
    cols = len(mat[0])
    # count how many index store first char of the word and store those in a 
    # start q
    for r in range(rows):
        for c in range(cols):
            if dfs(mat, r, c, 0, word):
                return True
    return False


"""

  10) Longest Palindromic Substring
  Topic: Dynamic Programming, String, Two Pointers
  Difficulty: Medium

  Given a string s, return the longest palindromic substring in s.

  Example
  Input: s = "babad"
  Output: "bab" (Note: "aba" is also a valid answer)
"""




if __name__ == "__main__":
    # intersection_of_two_arr_2([4,9,5], [9,4,9,8,4])
    # bt1 = create_bt([1,3,2,5])
    # bt2 = create_bt([2,1,3,None,4,None,7])
    # m_bt = merge_bts_itr(bt1, bt2)
    # tree_to_list(m_bt)
    # ll1 = create_ll([1,2,3,4,5])
    # rotated_ll1 = rotate_ll_right_by_k(ll1, 2)
    # print_linked_list(rotated_ll1)
    # permutation_of_s1_in_s2("oooo", "eidbaooo")
    # find_first_and_last([5,7,7,8,8,10], 8)
    # decode_encoded_word("3[a2[c]]")
    # partion_labels("ababcbacadefegdehijhklij")
    board = [
          ["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]
        ]
    word = "ABCCED"
    search_word_in_matrix(board, word)
    
