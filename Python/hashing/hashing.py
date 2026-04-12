# Hashing questions 

def return_count_of_intersection_of_two_arr(list1: list, list2: list) -> int:
    res = 0
    set1 = set()
    for elm in list1:
        set1.add(elm)
    for elm in list2:
        if elm in set1:
            res += 1
            set1.remove(elm)
    return res
def union_size(list1: list, list2: list) -> int:
    m = len(list1)
    n = len(list2)
    res = 0
    temp_arr = [0] * (m + n)

    for i in range(m):
        temp_arr[i] = list1[i]
    for i in range(n):
        temp_arr[m+i] = list2[i]

    for i in range(m+n):
        flag = False
        for j in range(i):
            if temp_arr[j] == temp_arr[i]:
               flag = True 
               break
        if flag == False:
            res += 1
    return res

def union_size_efc(list1: list, list2: list) -> int:
    unique_items = set()
    for elm in list1:
        unique_items.add(elm)
    for elm in list2:
        unique_items.add(elm)
    return len(unique_items)

def union_size_v2(list1: list , list2: list) -> int:
    temp = [] 
    m = len(list1)
    n = len(list2)
    res = 0
    for i in range(m):
        temp.append(list1[i])
    for i in range(n):
        temp.append(list2[i])
    for i in range(m+n):
        flag = False
        for j in range(i):
            if temp[i] == temp[j]:
                flag = True
                break
        if flag == False:
            res += 1
    return res

def pair_sum(list1: list, sum: int) -> bool:
    u_set = set()
    """
    for elm = 3 , sum - 3 i.e 14 which not in u_set , add 3 to u_set
    for elm = 2 , sum - 2 i.e 15 which in not in u_set , add 2 to u_set
    for elm = 8 , sum - 8 i.e 9 which is not in u_set, add 8 to u_set
    u_set = {3 ,2, 8}
    for elm = 15 , sum - 15 i.e 2 which is present in u_set , return true or 
    or we can also return 2, 15 , or index of 2(1) and 15(3)
    """
    for elm in list1:
        if (sum - elm) in u_set:
            return True
        u_set.add(elm)
    
    return False

def return_0_subarray_sum(list1: list) -> bool:
    m = len(list1)
    for i in range(m):
        for j in (i+1, m+1):
            if sum(list1[i:j]) == 0:
                return True
    return False

def subarray_sum_0(list1: list) -> bool:
    """

    """
    m = len(list1)
    u_set = set()
    pre_sum = 0
    for i in range(m):
        pre_sum += list1[i]
        if pre_sum == 0 or pre_sum in u_set:
            return True
        u_set.add(pre_sum)
    return False

def calculate_sub_array_with_given_sum(l: list, target: int) -> bool:
    s, curr = 0, 0
    for e in range(len(l)):
        curr += l[e]
        while s <= e and curr > target:
            curr -= l[s]
            s += 1
        if curr == target:
            return True
    return False

def two_sum_idx(arr: list[list], target: int) -> list[int]:
    u_map = {}
    for i, num in enumerate(arr):
        if (target - num) in u_map:
            return [u_map.get(target - num), i]
        else:
            u_map[num] = i
    return []

def contain_duplicates(nums: list[int]) -> bool:
    u_set = set()
    for num in nums:
        if num in u_set:
            return True
        u_set.add(num)
    return False
                  

if __name__ == "__main__":
    print(contain_duplicates([1,2,3,4]))