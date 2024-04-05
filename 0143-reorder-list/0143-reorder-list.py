# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         def reverse(head):
#             prev = None
#             while head:
#                 next_node = head.next
#                 head.next = prev
#                 prev = head
#                 head = next_node
#             return prev
        
#         if not head or not head.next:
#             return # head
        
#         # get to the middle of the LL
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         # reverse from middle->end of LL
#         head_second_half = reverse(slow)
        
#         # rearrange to produce LL in the required order
#         head_first_half = head
#         while head_second_half:
#             temp1 = head_first_half.next
#             temp2 = head_second_half.next
#             head_first_half.next = head_second_half
#             head_second_half.next = temp1
#             head_first_half = temp1
#             head_second_half = temp2
            
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        if not head or not head.next:
            return

        # get to the middle of the LL
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from middle->end of LL
        head_second_half = reverse(slow.next)
        slow.next = None  # break the link between first and second half

        # rearrange to produce LL in the required order
        head_first_half = head
        while head_second_half:
            temp1, temp2 = head_first_half.next, head_second_half.next
            head_first_half.next = head_second_half
            head_second_half.next = temp1
            head_first_half, head_second_half = temp1, temp2

         
        
        