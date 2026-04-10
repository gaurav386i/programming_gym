from two_pointers import ListNode
 

def print_linked_list(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print("-->".join(res))

"""
2) Find the Middle of a Linked List

Topic: Slow and Fast Pointers
Difficulty: Easy
Given the head of a singly linked list, return the middle node. 
If there are two middle nodes, return the second one.
"""
def find_middle_node_of_ll(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

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
    

    print_linked_list(head0)
    mid_node = find_middle_node_of_ll(head0)
    print(mid_node.val)
