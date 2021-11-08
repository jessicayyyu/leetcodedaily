import collections
from collections import deque
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q = deque([(root, 0)])
    res = collections.defaultdict(list)
    while q:
        node, col = q.popleft()
        res[col].append(node.val)
        if node.left:
            q.append((node.left, col-1))
        if node.right:
            q.append((node.right, col+1))
    #return [res[i] for i in sorted(res)]
    return [x[1] for x in sorted(res.items(), key=lambda x:x[0])]

