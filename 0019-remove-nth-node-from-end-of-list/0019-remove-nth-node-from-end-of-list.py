# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # time complexity - O(n)
        # space complexity - O(1)
        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next
        prev = p1
        if not p2:
            return head.next
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        if prev and p1:
            prev.next = p1.next
        return head

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # get the length of the linked list
#         temp = head
#         size = 0
#         while temp:
#             size += 1
#             temp = temp.next
#         print("size is:",size)
#         # subtract n from length to get the node to remove
#         node_to_remove = size - n
#         print("node to nremove is:",node_to_remove)
#         # remove the node
#         count = 0
#         dummy_head = ListNode(0)
#         dummy_head = head
#         print(dummy_head)
#         while dummy_head:
#             if count != node_to_remove:
#                 dummy_head = dummy_head.next
#             else:
#                 dummy_head = dummy_head.next.next
#             count += 1
#         print(head)
#         return dummy_head