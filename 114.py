def flatten(self, root: TreeNode) -> None:
    self.dfs(root)

def dfs(self, root):
    if not root:
        return []
    left_last_node = self.dfs(root.left)
    right_last_node = self.dfs(root.right)
    if left_last_node:
        left_last_node.right = root.right
        root.right = root.left
        root.left = None
    return right_last_node or left_last_node or root