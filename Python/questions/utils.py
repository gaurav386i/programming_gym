from collections import deque
from typing import Optional, List, Any


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


def create_bt(arr: List[Any]) -> Optional[TreeNode]:
    """
    Convert level-order list representation of a binary tree
    into an actual binary tree.

    Example:
    [10, 5, 15, 3, 7, None, 18]
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def create_ll(arr: List[int]) -> Optional[Node]:
    """
    Convert list representation into a linked list.

    Example:
    [1, 2, 3, 4]
    """
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next

    return head
