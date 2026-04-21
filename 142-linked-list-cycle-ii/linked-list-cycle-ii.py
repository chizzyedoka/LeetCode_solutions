# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # determine cycle exits
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return None
            
            slow = slow.next
            fast = fast.next.next

        # get length of cycle
        cycle_length = 1
        fast = fast.next
        while slow != fast:
            cycle_length += 1
            fast = fast.next

        # find cycle
        p1 = head
        p2 = head

        for _ in range(cycle_length):
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1