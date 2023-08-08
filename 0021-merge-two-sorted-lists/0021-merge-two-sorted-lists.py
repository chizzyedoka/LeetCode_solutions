# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        head = list3
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        #if list1 and not list2:
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        #if list2 and not list1:
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next
        return list3.next
            
                
        