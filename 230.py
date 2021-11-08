def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    traversallist = self.dfs([], root)
    return traversallist[k-1]

def dfs(self, traversallist, root):
    if not root:
        return
    self.dfs(traversallist, root.left)
    traversallist.append(root.val)
    self.dfs(traversallist, root.right)
    return traversallist