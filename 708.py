"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        prev, cur = head, head.next
        while prev.next != head:
            if prev.val <= node.val <= cur.val:
                break
            if prev.val > cur.val and (node.val > prev.val or node.val < cur.val):
                break
            prev, cur = prev.next, cur.next
        node.next = cur
        prev.next = node
        return head