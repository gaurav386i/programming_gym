"""
Given a string s, find the length of the longest substring without repeating 
characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: "abc"
"""
def longest_substring_without_repeating_char(input: str) -> str:
    s = 0
    for ed in range(1, len(input)):

        sub_string = input[s:ed]


"""
Given two strings s and t, return the minimum window in s which contains all 
the characters of t. If no such window exists, return an empty string.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""