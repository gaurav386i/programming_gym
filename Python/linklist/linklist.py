"""
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list. If the number of nodes is not a multiple of k, 
leave the remaining nodes as they are.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 2 -> 1 -> 4 -> 3 -> 5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


def reverse_k_nodes_of_linklist(head: ListNode) -> ListNode:
    pass