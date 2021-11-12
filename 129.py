# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, prevSum):
        if not root:
            return 0
        sum = root.val + prevSum*10
        if not root.left and not root.right:
            return sum
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)