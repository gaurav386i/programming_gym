"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""
def product_of_all_except_self(arr: list[int]) -> list[int]:
    n = len(arr)
    prefix = 1
    result = [1] * n
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]
    print(result)
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        print(result)
        suffix *= arr[i]
    return result 

def product_of_all_except_self_v2(arr: list[int]) -> list[int]:
    n = len(arr)
    prefix = 1
    result = [1] * n
    for i in range(n):
        result[i]  = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(n):
        result[i] *= suffix
        suffix *= arr[i]
    return result

if __name__ == "__main__":
    print(product_of_all_except_self([1,2,4,6]))
