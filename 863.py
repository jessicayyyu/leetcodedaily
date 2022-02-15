# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parents = {}
        q = deque([(target, 0)])
        visited = set()
        visited.add(target)
        res = []
        self.dfs(root, parents)
        while q:
            node, L = q.popleft()
            if L == k:
                res.append(node.val)
            if node.left and node.left not in visited:
                q.append((node.left, L + 1))
                visited.add(node.left)
            if node.right and node.right not in visited:
                q.append((node.right, L + 1))
                visited.add(node.right)
            if node in parents and parents[node] not in visited:
                q.append((parents[node], L + 1))
                visited.add(parents[node])
        return res

    def dfs(self, root, parents):
        if not root:
            return None
        if root.left:
            parents[root.left] = root
            self.dfs(root.left, parents)
        if root.right:
            parents[root.right] = root
            self.dfs(root.right, parents)
