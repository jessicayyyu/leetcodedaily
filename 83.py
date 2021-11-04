def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    dummy = head
    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return dummy