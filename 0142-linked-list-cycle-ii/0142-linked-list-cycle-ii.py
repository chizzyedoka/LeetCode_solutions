# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         hashMap = {}
#         while temp:
#             if temp in hashMap:
#                 return temp
#             hashMap[temp] = True
#             temp = temp.next
#         return None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        ptrOne = head
        while ptrOne != slow:
                ptrOne = ptrOne.next
                slow = slow.next
        return ptrOne
    
    
    