# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        nums = []
        self.inorderTraverse(root, nums)
        return self.dfs(nums, 0, len(nums)-1)

    def inorderTraverse(self, root, nums):
        if not root:
            return
        self.inorderTraverse(root.left, nums)
        nums.append(root.val)
        self.inorderTraverse(root.right, nums)

    def dfs(self, nums, start, end):
        if start > end:
            return
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid-1)
        root.right = self.dfs(nums, mid+1, end)
        return root