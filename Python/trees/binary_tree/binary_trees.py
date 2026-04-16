"""
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.

List based tree :

root at index 0
left child of index i → 2*i + 1
right child of index i → 2*i + 2
parent of index i → (i - 1) // 2

"""
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

def valid_bst(root: Node) -> bool:
    if root == None:
        return True
    if root.left and root.key < root.left.key:
        return False
    elif root.right and root.key > root.right.key:
        return False
    elif root.left and root.key > root.left.key:
        return True
    elif root.right and root.key < root.right.key:
        return True
    else:
        return valid_bst(root.left) and valid_bst(root.right)


def are_bsts_same(root1: Node, root2: Node):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.key != root2.key:
        return False
    else:
        return are_bsts_same(root1.left, root2.left) and are_bsts_same(
            root1.right, root2.right
        )


def level_order_traversal(root: Node) -> None:
    if not root:
        return None
    q = deque()
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


if __name__ == "__main__":
    root1 = Node(10)
    n1 = Node(9)
    n2 = Node(30)
    n3 = Node(40)
    
    root1.left = n1
    root1.right = n2
    n2.right = n3
    
    print(level_order_traversal(root1))
