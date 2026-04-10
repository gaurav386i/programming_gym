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


"""
8) Search in a Binary Search Tree

Topic: Binary Search Tree
Difficulty: Easy
Given the root of a BST and a value, return the node where the value exists. 
If it does not exist, return null.
"""
def search_BST_for_node(root: Node, value) -> Node:
    if root == None:
        return None
    if root.key == value:
        return root
    elif value < root.key:
        return search_BST_for_node(root.left, value)
    else:
        return search_BST_for_node(root.right, value)

def search_BST_iterative(root: Node, value: int) -> Node | None:
    curr = root
    while curr:
        if curr.key == value:
            return curr
        elif curr.key < value:
             curr = curr.right
        else:
            curr = curr.left
    return None

if __name__ == "__main__":
    root1 = Node(10)
    n1 = Node(20)
    n2 = Node(30)
    n3 = Node(40)
    
    root1.left = n1
    root1.right = n2
    n1.left = n3
    node_value = search_BST_iterative(root1, 30)
    print(node_value.key)
