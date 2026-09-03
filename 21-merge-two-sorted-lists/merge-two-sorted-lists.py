# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        pointerOne = list1
        pointerTwo = list2
        head = dummy

        while pointerOne and pointerTwo:
            if pointerOne.val < pointerTwo.val:
                head.next = pointerOne
                pointerOne = pointerOne.next
            else:
                head.next = pointerTwo
                pointerTwo = pointerTwo.next
            head = head.next

        if pointerOne:
            head.next = pointerOne
        else:
            head.next = pointerTwo
        return dummy.next