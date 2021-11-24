import sys
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    if not root:
        return 0
    self.counter = -sys.maxsize
    self.dfs(root)
    return self.counter

def dfs(self, root):
    if not root:
        return 0
    left = self.dfs(root.left)
    right = self.dfs(root.right)
    self.counter = max(self.counter, left + right)
    return max(1+left, 1+right)