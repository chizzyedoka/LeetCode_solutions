# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        hashMap = {}
        while temp:
            if temp in hashMap:
                return temp
            hashMap[temp] = True
            temp = temp.next
        return None
            
        
        
        # slow = head
        # fast = head
        # cycle_length = 0
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         current = slow
        #         while current.next != slow:
        #             current = current.next
        #             cycle_length += 1
        #     ptrOne = head
        #     ptrTwo = head
        #     while cycle_length > 0:
        #         ptrTwo = ptrTwo.next
        #         cycle_length -= 1
        #     while ptrOne != ptrTwo:
        #         ptrOne = ptrOne.next
        #         ptrTwo = ptrTwo.next
        #     return ptrOne
        # return None
    
    