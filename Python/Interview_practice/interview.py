class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
There is an unsorted intger array, calculate longest subarray of consecutive 
integers
"""

def longest_consecutive_sub_arr(arr: list[int]) -> list[int]:
    if not arr:
        return []
    u_arr = set(arr)
    best_start = 0
    best_len = 0

    for num in arr:
        if num - 1 not in u_arr:
            curr = num
            lenth = 0

            while num + 1 in u_arr:
                curr = num + 1
                lenth += 1
            if lenth > best_len:
                best_len = lenth
                best_start = curr
    return []



def reverse_k_nodes_in_linklist(head: ListNode, kth: int) -> ListNode:
    if not head or kth <= 1:
        return head
    dummy = ListNode(0)
    dummy.next = head
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    group_prev = dummy

    while count <= kth:
        curr = group_prev.next
        prev = None
        next_group_head = curr
        for _ in range(kth):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        tail = next_group_head
        group_prev.next = prev
        tail.next = curr

        group_prev = tail

        count -= kth
    return dummy.next


def sub_arr_of_longest_consecutive_int():
    pass

            


if __name__ == "__main__":
    arr1 = [1, 9, 2, 3 ,4 , 6 , 7, 5]
    print(longest_consecutive_sub_arr(arr1))