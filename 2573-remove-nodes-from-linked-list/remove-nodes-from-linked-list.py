# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        current = stack.pop()
        max_node = current.val
        result = ListNode(max_node)

        while stack:
            current = stack.pop()
            if current.val >= max_node:
                max_node = current.val
                new_node = ListNode(current.val)
                new_node.next = result
                result = new_node

        return result

