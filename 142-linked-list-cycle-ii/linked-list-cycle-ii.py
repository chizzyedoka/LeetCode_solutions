# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        seen = set()

        while current:
            if current.next is None:
                return None
            if current in seen:
                return current
            seen.add(current)
            current = current.next