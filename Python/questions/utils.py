def print_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_linklist(ll: Node) -> None:
    res = []
    curr = ll
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print("->".join(res))
