from heapq import heappush, heappop


"""
7) Top K Frequent Elements

Topic: Heaps
Difficulty: Medium
Given an integer array and an integer k, return the k most frequent elements.
"""
def top_k_frequent_element(arr: list[int], top_k) -> list[int]:
    if top_k <= 0:
        return []
    max_heap = []
    freq = {}
    resp = []
    for elm in arr:
        freq[elm] = freq.get(elm, 0) + 1
    
    
    for k,v in freq.items():
        heappush(max_heap, (-v, k))
    for _ in range(min(top_k, len(freq))):
        _, v = heappop(max_heap)
        resp.append(v)
    return resp

def kth_larget_element_in_an_arr(arr: list[int], kth: int) -> int:
    if kth <= 0:
        return 0
    max_heap = []
    for num in arr:
        heappush(max_heap, -num)
    for _ in range(kth - 1):
        _ = heappop(max_heap)
    return -heappop(max_heap)
    

if __name__ == "__main__":
    elms = [
        1,2,1,2,3,4,4,6,7,1,2,2,3,3,2,1,2,3,54,5,5,6,4,3,5,6,7,6,67,56,34,12,11,12,13,
        ]
    print(kth_larget_element_in_an_arr([3,2,3,1,2,4,5,5,6], 4))
