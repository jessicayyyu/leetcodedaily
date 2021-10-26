def isValidBST(self, root: Optional[TreeNode]) -> bool:
    isValid, minVal, maxVal = self.divideConquer(root)
    return isValid

def divideConquer(self, root):
    if not root:
        return True, None, None
    isLeft, leftMin, leftMax = self.divideConquer(root.left)
    isRight, rightMin, rightMax = self.divideConquer(root.right)
    if not isLeft or not isRight:
        return False, None, None
    if leftMax is not None and leftMax >= root.val:
        return False, None, None
    if rightMin is not None and rightMin <= root.val:
        return False, None, None
    minVal = leftMin if leftMin is not None else root.val
    maxVal = rightMax if rightMax is not None else root.val
    return True, minVal, maxVal