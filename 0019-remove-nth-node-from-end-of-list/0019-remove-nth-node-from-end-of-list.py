# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the length of the linked list
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        print("size is:",size)
        
        # subtract n from length to get the node to remove
        index_to_remove = size - n - 1
        print("index of node to remove is:",index_to_remove)
        
        # edge case
        if size == n:
            return head.next
        
        # remove the node
        curr = head
        for i in range(index_to_remove):
            curr = curr.next
            print(curr)
        curr.next = curr.next.next
        return head
        
        
        # count = 0
        # dummy = ListNode()
        # ptr = dummy
        # while head:
        #     if count != index_to_remove-1:
        #         ptr.next = head
        #         ptr = ptr.next
        #         head = head.next
        #     else:
        #         head = head.next
        #     count += 1
        # return dummy.next