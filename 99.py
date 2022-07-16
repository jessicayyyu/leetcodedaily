# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math


class Solution:
    import math
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        first, second = None, None
        prev = TreeNode(-math.inf)
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev.val:
                if not first:
                    first = prev
                    second = root
                else:
                    second = root
            prev = root
            root = root.right
        first.val, second.val = second.val, first.val

