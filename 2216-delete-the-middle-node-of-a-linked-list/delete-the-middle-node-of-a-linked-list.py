# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        list_length = 0
        current_node = head
        while current_node:
            list_length += 1
            current_node = current_node.next

        middle_length = list_length // 2
        count = 1
        current_node = head

        while count != middle_length and current_node.next:
            current_node = current_node.next
            count += 1

        if current_node.next:
            current_node.next = current_node.next.next

        return head

