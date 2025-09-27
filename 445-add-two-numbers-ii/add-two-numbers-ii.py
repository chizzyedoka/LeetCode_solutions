# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def reverseLL(head):
            if not head:
                return
           
            prev = None
            cur = head
            nxt = None
            while cur:
                # store the next node
                nxt = cur.next
                # reverse cur's node next pointer
                cur.next = prev
                # move pointer's one posiion ahead
                prev = cur
                cur = nxt
            return prev

        l1 = reverseLL(l1)
        l2 = reverseLL(l2)

        carry = 0
        l3 = ListNode()
        cur = l3
        while l1 and l2:
            curSum = l1.val + l2.val + carry
            carry = curSum // 10
            digit = curSum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            curSum = l1.val + carry
            carry = curSum // 10
            digit = curSum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next

        while l2:
            curSum = l2.val + carry
            carry = curSum // 10
            digit = curSum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        


        return reverseLL(l3.next)
            