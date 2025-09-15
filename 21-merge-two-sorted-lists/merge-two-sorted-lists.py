# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1 and not l2:
                current.next = l1
            
        elif l2 and not l1:
                current.next = l2
                
        
        return dummy.next