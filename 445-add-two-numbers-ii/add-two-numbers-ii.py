# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def reverseLL(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        # Reverse input lists
        l1 = reverseLL(l1)
        l2 = reverseLL(l2)

        carry = 0
        dummy = ListNode()
        cur = dummy

        # Add both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curSum = val1 + val2 + carry

            carry = curSum // 10
            digit = curSum % 10
            cur.next = ListNode(digit)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Reverse result back
        return reverseLL(dummy.next)
