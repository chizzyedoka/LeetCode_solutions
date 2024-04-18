# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        cur = head
        preLeft = dummy
        
        # get cur node to reverse from
        for i in range(left-1):
            cur =cur.next
            preLeft = preLeft.next
            
        subListHead = cur
        #  reverse sublist
        prev = None
        for i in range(right-left+1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        preLeft.next = prev
        subListHead.next = cur
        print(dummy.next)
        return dummy.next
        
        
        
        
        
        