import math

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

if __name__ == "__main__":
    root1 = Node(10)
    n1 = Node(30)
    n2 = Node(5)
    n3 = Node(90)
    n4 = Node(80)
    n5 = Node(70)
    root1.left = n1
    root1.right = n2
    n1.left = n3
    n2.left = n4
    n3.right = n5
    print(max_in_binary_tree(root1))
