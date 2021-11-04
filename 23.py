def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    return self.mergeLists(lists, 0, len(lists) -1)

def mergeLists(self, lists, start, end):
    if start == end:
        return lists[start]
    mid = (start + end)//2
    left = self.mergeLists(lists, start, mid)
    right = self.mergeLists(lists, mid+1, end)
    return self.mergeTwoLists(left, right)

def mergeTwoLists(self, head1, head2):
    dummy = ListNode(0)
    head = dummy
    while head1 and head2:
        if head1.val < head2.val:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    head.next = head1 or head2
    return dummy.next