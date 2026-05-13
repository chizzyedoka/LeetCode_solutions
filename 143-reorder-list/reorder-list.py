# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        def reverse_linked_list(node):
            prev = None
            current = node

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        def get_middle(node):
            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        middle_node = get_middle(head)
        second_half = reverse_linked_list(middle_node.next)

        # Break the list into two halves
        middle_node.next = None

        # merge
        first = head
        second = second_half

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
