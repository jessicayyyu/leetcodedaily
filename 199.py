from collections import  deque
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == size - 1:
                res.append(node.val)
    return res