def maxPathSum(self, root: TreeNode) -> int:
    self.maxSum = -sys.maxsize
    self.dfs(root)
    return self.maxSum


def dfs(self, root):
    if not root:
        return 0
    leftSum = self.dfs(root.left)
    if leftSum < 0:
        leftSum = 0

    rightSum = self.dfs(root.right)
    if rightSum < 0:
        rightSum = 0

    self.maxSum = max(self.maxSum, root.val + leftSum + rightSum)
    return max(root.val + leftSum, root.val + rightSum)