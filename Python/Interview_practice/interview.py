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



def reverse_k_nodes(head: ListNode, kth: int) -> ListNode:
    if not head:
        return head
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next
    dummy = ListNode(0, head)
    group_prev = dummy

    while count > kth:
        curr = group_prev.next
        prev = None
        for _ in range(kth):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tail = group_prev.next
        curr = tail.next
        group_prev.next = prev

        count -= kth
    return dummy.next

            


if __name__ == "__main__":
    arr1 = [1, 9, 2, 3 ,4 , 6 , 7, 5]
    print(longest_consecutive_sub_arr(arr1))