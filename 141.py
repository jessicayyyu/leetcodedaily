def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False