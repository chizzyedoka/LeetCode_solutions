# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         while k >0:
#             dummy = ListNode(-1)
#             dummy.next = head
#             first = head
#             while head.next:
#                 left = head
#                 head = head.next
#             left.next = None
#             head.next = first
#             k-=1
#         return dummy.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        # Calculate the length of the list and find the last node
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Calculate the actual rotation amount
        k %= length
        if k == 0:
            return head

        # Find the new tail and break the list at that point
        new_tail_idx = length - k - 1
        new_tail = head
        for _ in range(new_tail_idx):
            new_tail = new_tail.next

        # Perform the rotation
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
