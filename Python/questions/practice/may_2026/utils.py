from typing import List, Optional, Any
from collections import deque



class TreeNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None


def print_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)

        return result
    return wrapper


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


def create_ll(arr: List[int]) -> Optional[ListNode]:
    """
    Convert list representation into a linked list.

    Example:
    [1, 2, 3, 4]
    """
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head

def print_linked_list(head):
    temp = head
    res = []
    while temp:
        res.append(str(temp.val))
        temp = temp.next
    print("-->".join(res))


def tree_to_list(root):
    """
    Returns a level-order list representation of the binary tree.
    Prints 'No tree provided' if root is None.
    """
    if root is None:
        print("No tree provided")
        return None

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
            
    print(result)