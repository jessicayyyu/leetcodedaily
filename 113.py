def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    result = []
    self.dfs(root, sum, [], result)
    return result


def dfs(self, root, target, path, result):
    if not root:
        return
    path.append(root.val)
    target -= root.val
    if target == 0 and not root.left and not root.right:
        result.append(path[:])
        return
    self.dfs(root.left, target, path[:], result)
    self.dfs(root.right, target, path[:], result)