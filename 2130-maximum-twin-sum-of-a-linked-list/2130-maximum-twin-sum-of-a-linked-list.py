# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        lst1 = head # original list
        curr = head
        prev = None
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = prev  
            prev = new_node
            curr = curr.next
        lst2 = prev # reversed list
        maxTwinSum = float('-inf')
        count = 0
        while lst1:
            if count == length/2:
                break
            twinSum = lst1.val + lst2.val
            maxTwinSum = max(maxTwinSum, twinSum)
            lst1 = lst1.next
            lst2 = lst2.next
            count += 1
        return maxTwinSum

        