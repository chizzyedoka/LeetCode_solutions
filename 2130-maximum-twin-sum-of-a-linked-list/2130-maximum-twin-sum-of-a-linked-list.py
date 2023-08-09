# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Algorithm
# reverse the linked list without modifying the original linked list
# sum each position of the reversed list and the original
# save the maximum at each iteration
# return this maximum at the end

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst1 = head # original list
        # reverse linked list
        curr = head
        prev = None
        while curr:
            new_node = ListNode(curr.val) # create a new node
            new_node.next = prev  
            prev = new_node
            curr = curr.next
        lst2 = prev # reversed list
        maxTwinSum = float('-inf')
        count = 0
        while lst1:
            twinSum = lst1.val + lst2.val
            maxTwinSum = max(maxTwinSum, twinSum)
            lst1 = lst1.next
            lst2 = lst2.next
        return maxTwinSum

        