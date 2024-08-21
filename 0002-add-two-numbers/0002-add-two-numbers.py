# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        res = ListNode(0)
        cur = res
        carry = 0
        while h1 or h2 or carry:
            if h1: 
                d1 = h1.val 
            else: d1 = 0
            if h2: 
                d2 = h2.val 
            else: d2 = 0
                
            total = (d1 + d2 + carry)
            carry = total // 10
            digit = total % 10
            
            cur.next = ListNode(digit)
            cur = cur.next
            
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
            
        return res.next