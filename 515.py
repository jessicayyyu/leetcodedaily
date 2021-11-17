import sys
from collections import deque
def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        largest = -sys.maxsize
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            largest = max(largest, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(largest)
    return res

