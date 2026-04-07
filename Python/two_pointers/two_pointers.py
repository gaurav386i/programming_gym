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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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



if __name__ == "__main__":
    print(remove_one_char_to_make_palindrome("abca"))
    print(remove_one_char_to_make_palindrome("abcdefa"))

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
    while new_head:
          print(f"--->{new_head.val}", end="")
          new_head = new_head.next