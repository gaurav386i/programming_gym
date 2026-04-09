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


def reverse_k_nodes_of_linklist(head: ListNode, k: int) -> ListNode:
    cnt = 0
    temp = head
    dummy = ListNode(0, head)
    while temp:
        cnt += 1
        temp = temp.next
    if cnt < k:
        return head
    group_prev = dummy
    while cnt >= k:
        curr = group_prev.next
        prev = None

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        
    