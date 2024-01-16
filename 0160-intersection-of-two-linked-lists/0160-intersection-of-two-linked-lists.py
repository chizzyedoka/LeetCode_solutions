# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # using hashMap
        seen = set()
        aptr = headA
        bptr = headB
        while aptr:
            seen.add(aptr)
            aptr = aptr.next
        while bptr:
            if bptr in seen:
                return bptr
            bptr = bptr.next
        return None
        # l1 = headA
        # l2 = headB
        # while l1 != l2:
        #     if l1:
        #         l1 = l1.next
        #     else:
        #         l1 = headB
        #     if l2:
        #         l2 = l2.next
        #     else:
        #         l2 = headA
        # return l1
    
#         if headA is None or headB is None:
#             return None
        
#         intersection = set()
#         while headA is not None:
#             intersection.add(headA)
#             headA = headA.next
        
#         while headB is not None:
#             if headB in intersection:
#                 return headB
#             headB = headB.next
        
#         return Non