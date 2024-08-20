# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dh = head
        while dh and dh.next:
            if dh.val == dh.next.val:
                dh.next = dh.next.next
            else:
                dh = dh.next
        return head