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


"""
## 7) Insert Interval

**Topic:** Intervals
**Difficulty:** Medium

You are given an array of non-overlapping intervals `intervals` where 
`intervals[i] = [starti, endi]` represent the start and the end of 
the `i`th interval and `intervals` is sorted in ascending order 
by `starti`. You are also given an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` 
is still sorted in ascending order by `starti` and still does 
not have any overlapping intervals.

Return `intervals` after the insertion.

### Example 1

**Input:**
`intervals = [[1,3],[6,9]], newInterval = [2,5]`
**Output:**
`[[1,5],[6,9]]`
"""


def insert_and_merge_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    n = len(intervals)
    i = 0
    resp = []
    # add all intervals greater that new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        resp.append(intervals[i])
        i += 1
    # merge all overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    # append merged
    resp.append(new_interval)

    # add remaining interval
    while i < n:
        resp.append(intervals[i])
        i += 1
    return resp


if __name__ == "__main__":

    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert_and_merge_interval(intervals, newInterval))
