def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    q = deque([(root, 0, 0)])
    result = []
    level = collections.defaultdict(list)
    while q:
        node, row, col = q.popleft()
        level[col].append((node.val, row))
        if node.left:
            q.append((node.left, row + 1, col - 1))
        if node.right:
            q.append((node.right, row + 1, col + 1))
    for col in sorted(level.keys()):
        vals = [x[0] for x in sorted(level[col], key=lambda x: (x[1], x[0]))]
        result.append(vals)
    return result