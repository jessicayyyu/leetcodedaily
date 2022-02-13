# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        subtree = []
        total = self.dfs( root, subtree)
        res = 0
        for s in subtree:
            res = max(res, s*(total - s))
        return res %(10**9 + 7)

    def dfs(self, root, subtree):
        if not root:
            return 0
        leftsum = self.dfs(root.left, subtree)
        rightsum = self.dfs(root.right, subtree)
        total = leftsum + rightsum + root.val
        subtree.append(total)
        return total