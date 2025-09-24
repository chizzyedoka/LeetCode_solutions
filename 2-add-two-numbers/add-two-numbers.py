# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

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
        return dummy.next