from collections import deque

def serialize(self, root):
    if root is None:
        return ""
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        if node:
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            result.append("#")
    return " ".join(result)

def deserialize(self, data):
    if not data:
        return None
    treedata = data.split(' ')
    root = TreeNode(int(treedata[0]))
    q = [root]
    isLeft, index = True, 0
    for val in treedata[1:]:
        if val is not "#":
            node = TreeNode(int(val))
            if isLeft:
                q[index].left = node
            else:
                q[index].right = node
        if not isLeft:
            index += 1
        isLeft = not isLeft
    return root


