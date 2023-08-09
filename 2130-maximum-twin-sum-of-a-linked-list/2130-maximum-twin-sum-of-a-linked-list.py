# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst1 = head
        curr = head
        prev = None
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = prev  
            prev = new_node
            curr = curr.next
        lst2 = prev
        
        maxTwinSum = float('-inf')
        while lst1:
            twinSum = lst1.val + lst2.val
            maxTwinSum = max(maxTwinSum, twinSum)
            lst1 = lst1.next
            lst2 = lst2.next
        
        return maxTwinSum
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         lst1 = head
#         curr = head
#         prev = None
#         while curr:
#             new_node = ListNode(curr.val)
#             new_node.next = prev  
#             prev = new_node
#             curr = curr.next
#         lst2 = prev
#         print(lst2)
#         print(lst1 )
#         maxTwinSum = float('-inf')
#         while lst1:
#             twinSum = lst1.val + lst2.val
#             maxTwinSum = max(maxTwinSum,twinSum)
#             lst1 = lst1.next
#             lst2 = lst2.next
#         return maxTwinSum

        