class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given a string s, return true if it can become a palindrome after deleting at 
most one character, otherwise return false.

Example:
Input: "abca"
Output: true
Explanation: Remove 'b' or 'c'.
"""
def remove_one_char_to_make_palindrome(s: str) -> bool:
    st = 0
    ed = len(s) - 1
    count = 0
    while st < ed:
        if s[st] == s[ed]:
            st += 1
            ed -= 1
        if s[st] != s[ed]:
            count += 1
            st += 1
            ed -= 1
    if count > 1:
        return False
    return True

"""
Given the head of a singly linked list, remove the nth node from the end and 
return the head of the modified list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
Output: 1 -> 2 -> 3 -> 5
"""


def remove_nth_node_from_ll(head: ListNode, k=2) -> ListNode:
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return head

"""
3) Move Zeroes

Topic: Array / Two Pointers
Difficulty: Easy
Given an integer array, move all 0s to the end while keeping the relative 
order of non-zero elements. Do this in place.
"""
def move_zeroes_to_end(zeroes: list) -> list:
    j = 0

    for i in range(len(zeroes)):
        if zeroes[i] != 0:
            zeroes[j], zeroes[i] = zeroes[i], zeroes[j]
            j += 1
    return zeroes


"""
4) Two Sum in a Sorted Array

Topic: Two Pointers
Difficulty: Easy
Given a sorted array and a target sum, return the indices of the two numbers 
such that they add up to the target.

"""
def two_sum(arr: list, target: int) -> tuple[int, int]:
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        if arr[p1] + arr[p2] < target:
            p1 += 1
        elif arr[p1] + arr[p2] > target:
            p2 -= 1
        elif arr[p1] + arr[p2] == target:
            return (p1, p2)

def valid_palindrome_after_lower(sentence: str) -> bool:
    sentence = sentence.lower()
    start = 0
    end = len(sentence) - 1
    while start < end:
        if sentence[end] == sentence[start]:
            start += 1
            end -= 1
        else:
            return False


def remove_nth_node_from_end_of_list(head: ListNode, kth: int) -> ListNode:
    slow = head
    fast = head
    for _ in range(kth):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head



if __name__ == "__main__":

    head = ListNode(val=1)
    n1 = ListNode(val=2)
    n2 = ListNode(val=3)
    n3 = ListNode(val=4)
    n4 = ListNode(val=5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    new_head = remove_nth_node_from_ll(head)
    
    zeroes_arr = [1, 2, 0, 4, 0, 0, 5, 6, 0, 0, 7]
    sorted_arr = [1, 3, 5 ,7 ,9 , 10]
    target = 8
    # print(two_sum(sorted_arr, target))
    print(valid_palindrome_after_lower("A man, a plan, a canal: Panama"))
    print(valid_palindrome_after_lower("race a car"))