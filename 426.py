def treeToDoublyList(self, root: 'Node') -> 'Node':
    if not root:
        return None
    #iterative
    prev, first = None, None
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not first:
            first = root
        if prev:
            prev.right = root
            root.left = prev
        prev = root
        root = root.right
    first.left = prev
    prev.right = first
    return first


