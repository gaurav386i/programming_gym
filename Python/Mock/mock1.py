from collections import deque


"""
You’re given numCourses and prerequisites [a, b] meaning “take b before a.” 
Return whether you can finish all courses

numCourse = 3 [[a, b], [b, c]]

"""

def can_pass(numCourse: int, prerequisites: list[list[int]]) -> bool:
    if not numCourse or not prerequisites:
        return False
    
    graph = {i: [] for i in range(numCourse)}
    indegrees = [0] * numCourse

    for c, p in prerequisites:
        graph[p].append(c)
        indegrees[c] += 1
    q = deque()

    for i in indegrees:
        if i == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for nei in graph[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    return result if len(result) == numCourse else []


class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
   

def invert_bt(root: TreeNode) -> TreeNode:
    if root is None:
        return root
    st = [root]
    while st:
        node = st.pop()
        node.left, node.right = node.right, node.right
        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)
    return root
   

if __name__ == "__main__":
    print(can_pass(2, [[1,0]]))