# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        if not root:
            return None
        stack = []
        node, prev = root, None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                cur = stack.pop()
                if cur == p:
                    prev = cur
                elif prev:
                    return cur
                node = cur.right
        return



