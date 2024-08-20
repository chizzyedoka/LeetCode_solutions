# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         last_unduplicated_node = cur
#         while cur and cur.next:
#             if cur.val != cur.next.val:
#                 last_unduplicated_node = cur
#                 cur = cur.next
#             else:
#                 while cur.val == cur.next.val:
#                     cur = cur.next
#                 last_unduplicated_node.next = cur.next
#                 cur = cur.next
#         return head
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where the first node is duplicated
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # Skip all nodes with the same value
                duplicate_val = cur.next.val
                while cur.next and cur.next.val == duplicate_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next