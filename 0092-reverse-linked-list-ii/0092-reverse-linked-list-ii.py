# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m-1): p = p.next
        tail = p.next

        for i in range(n-m):
            tmp = p.next                  # a)
            p.next = tail.next            # b)
            tail.next = tail.next.next    # c)
            p.next.next = tmp             # d)
        return dummy.next
        # def reverse(head,left, right):
        #     prev = left
        #     cur = head
        #     while cur  != right:
        #         next = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = next
        #     return prev
        # temp = head
        # while temp:
        #     if temp.val == left:
        #         temp.next = reverse(temp,left,right)
        #     else:
        #         temp = temp.next
        # return head
        
        
        