def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    upper, lower = root, root
    while root:
        if root.val > target:
            upper = root
            root = root.left
        elif root.val < target:
            lower = root
            root = root.right
        else:
            return root.val
    if abs(upper.val - target) < abs(lower.val - target):
        return upper.val
    return lower.val