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
Given two strings s and t, return the minimum window in s which contains all 
the characters of t. If no such window exists, return an empty string.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""

if __name__ == "__main__":
    print(longest_substring_without_repeating_char("abcabcbb"))
