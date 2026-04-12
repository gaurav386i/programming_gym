# Sliding windows works like one element removed from windows and 
# one element is added to the window always keep in mind
#
#


"""
Given a string s, find the length of the longest substring without repeating 
characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: "abc"
"""
def longest_substring_without_repeating_char(input: str) -> int:
    left = 0
    last_seen = {}
    best_start = 0
    best_length = 0
    for right, ch in enumerate(input):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right

        curr_len = right - left + 1
        if curr_len > best_length:
            best_length = curr_len
            best_start = left
    """
    left = 0, right = 0, ch = a , last_seen = {"a": 0}, curr_len = 1, best_len = 1, best_start = 0
    left = 0, right = 1, ch = b, last_seen = {"a": 0, "b": 1}, curr_len = 2, best_len = 2, best_s = 0
    left = 0, right = 2, ch = c, last_seen = {"a": 0, "b": 1, "c": 2}, curr_len = 3,best_len = 3 , best_s = 0
    left = 1 , right = 3, ch = a, last_seen = {"a": 3, "b":1, "c": 2}, curr_len = 3 ,best_len = 3, best_s = 1
    left = 2, right = 4, ch = b, last_seen = {"a": 3, "b": 4, "c": 2, } curr_len = 3, best_len = 3, best_s = 1
    left = 3, right = 5, ch = c , last_seen = {"a": 3, "b": 4, "c": 5}, curr_len = 3, lest_len = 3, best_s = 1
    left = 5, right = 6, ch = b, last_seen = {"a": 3, "b": 6, "c": 5}, curr_len = 2, best_len = 3, best_s = 1
    left = 6, right = 7, ch = b, last_seen = {"a": 3, "b": 7, "c": 5}, curr_len = 2, best_len = 3, best_s = 1
    """
    return len(input[best_start: best_start + best_length])

"""
6) Maximum Sum Subarray of Size K

Topic: Sliding Window
Difficulty: Medium
Given an array of integers and an integer k, find the maximum sum of any 
contiguous subarray of size k.
"""

def max_subarr_sum(arr: list, k: int) -> int:
    if k <= 0 or k > len(arr):
        return 0
    p1 = 0
    p2 = k
    window_sum = sum(arr[:p2])
    max_sum = window_sum
    while p2 <= len(arr) - 1:
        
        window_sum += arr[p2] - arr[p1]
        max_sum = max(max_sum, window_sum)
        p2 += 1
        p1 += 1    
    return max_sum

def max_subarr_sum_for_loop_v(arr: list, k: int) -> int:
    if k <= 0 or k > len(arr):
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def longest_substring_without_repeated_chars(word: str) -> int:
    """
    we need best start if we have to return substring without repeated char
    otherwise if need to just calculate best_len can do.
    """
    left = 0
    best_start = 0
    last_seen = {}
    best_len = 0
    for right,  ch in enumerate(word):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        curr_len = right - left + 1

        if curr_len > best_len:
            best_len = curr_len
            best_start = left

    return  len(word[best_start: best_start + best_len])

def create_hash_str(st: str) -> dict:
    u_map = {}
    for ch in st:
        u_map[ch] = u_map.get(ch, 0) + 1
    return u_map


def permutation_in_string(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    if len(s1) > len(s2):
        return False
    needed = create_hash_str(s1)
    window = create_hash_str(s2)
    if needed == window:
        return True
    for i in range(n1, n2):
        window[s2[i]] += 1

        left_char = s2[i - 1]
        window[s2[left_char]] -= 1
        
        if window[left_char] == 0:
            del window[left_char]
        if window == needed:
            return True
    return False


"""
Given two strings s and t, return the minimum window in s which contains all 
the characters of t. If no such window exists, return an empty string.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""

if __name__ == "__main__":
    print(longest_substring_without_repeating_char("abcabcbb"))

    sum_arr = [3, 5, 2, 6, 19, 0, 25 , 2, 4, 13]
    sum_ar1 = [1, 6, -5, -2, -8, 9, -10, 11, -13, 14]

    print(longest_substring_without_repeated_chars("abcabcbb"))
