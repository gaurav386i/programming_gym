class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def prepare_ll(l: list) -> ListNode:
    """
    Create a linklist from list of integers
    """
    pass

def print_linked_list(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print("-->".join(res))


"""
1) Reverse a Singly Linked List

Topic: Linked List
Difficulty: Easy
Given the head of a singly linked list, reverse the list and return the new head.
"""
def reverse_ll(head: ListNode) -> ListNode:
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev



"""
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list. If the number of nodes is not a multiple of k, 
leave the remaining nodes as they are.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 2 -> 1 -> 4 -> 3 -> 5
"""



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
        
        tail = group_prev.next
        tail.next = curr
        group_prev.next = prev


        group_prev = tail

        count -= k
    return dummy.next


def detect_cycle_ll(head: ListNode) -> ListNode | None:
    if not head:
        return head
    slow = head
    fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = fast
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
    



if __name__ == "__main__":
    head0 = ListNode(10)
    n2 = ListNode(5)
    n3 = ListNode(7)
    n4 = ListNode(4)
    n5 = ListNode(13)

    head0.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3
    # print_linked_list(head0)
    # rev_head = reverse_ll(head0)
    # print_linked_list(rev_head)
    print(detect_cycle_ll(head0))

