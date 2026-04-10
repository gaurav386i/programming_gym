import math
from collections import deque
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def max_in_binary_tree(root: Node) -> int:
    if root == None:
        return -math.inf
    else:
        return max(
            root.key,
            max_in_binary_tree(root.left), 
            max_in_binary_tree(root.right)
            )
    
def print_level_order_traversal_line_by_line(root: Node) -> None:
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    while len(q) > 0:
        node = q.popleft()
        if node == None:
            print()
            q.append(None)
            continue
        print(node.key, end=" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

def print_bt_level_line_by_line_v2(root: Node) -> None:
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for _ in range(count):
            node = q.popleft()
            print(node.key, end=" ")
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print()
        

if __name__ == "__main__":
    root1 = Node(10)
    n1 = Node(20)
    n2 = Node(30)
    n3 = Node(40)
    
    root1.left = n1
    root1.right = n2
    n1.left = n3
    print_bt_level_line_by_line_v2(root1)
