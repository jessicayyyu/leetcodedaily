# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
# DFS Version
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if not root:
            return
        if root.left:
            self.dfs(root.left, res)
        res.append(root.val)
        if root.right:
            self.dfs(root.right, res)
#Iterative version
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res