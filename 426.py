def treeToDoublyList(self, root: 'Node') -> 'Node':
    if not root:
        return None
    head, tail = self.dfs(root)
    tail.right = head
    head.left = tail

    return head


def dfs(self, root):
    if not root:
        return None, None
    left_head, left_tail = self.dfs(root.left)
    right_head, right_tail = self.dfs(root.right)

    if left_tail:
        left_tail.right = root
        root.left = left_tail

    if right_head:
        right_head.left = root
        root.right = right_head

    head = left_head or root
    tail = right_tail or root

    return  head, tail

