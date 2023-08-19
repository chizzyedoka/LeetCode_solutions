# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         curr = slow
#         prev = None
#         while curr.next:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         start = head
#         while prev and prev.next:
#             if start.next != prev.next:
#                 return False
#             start = start.next
#             prev = prev.next
#         print(prev)
#         print(start)
#         if prev.next is None:
#             return False
#         return True
            
            
        