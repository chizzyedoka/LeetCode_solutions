# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,begin:ListNode, end:ListNode):
        prev = begin
        cur = begin.next
        first = cur
        while cur != end:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        begin.next = prev
        first.next = cur
        return first
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i%k==0:
                begin = self.reverse(begin,head.next)
                head = begin.next
            else:
                head = head.next
        return dummy.next
        
        