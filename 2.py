# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            num += carry
            digit, carry = num%10, num//10
            node = ListNode(digit)
            tail.next, tail = node, node
        return dummy.next