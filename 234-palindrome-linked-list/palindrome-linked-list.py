# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # base case
        if not head:
            return True

        # get the end of first half of the list
        def first_half_end(node):
            slow, fast = node, node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # reverse second half of list
        def reverse_ll(node):
            #         1 -> 2 -> 3 -> null
            # null <- 1 <- 2 <- 3
            prev = None
            cur = node
            while cur:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return prev

        dummy_head = head
        middle_node = first_half_end(dummy_head)
        second_half =  reverse_ll(middle_node.next)
        # use two pointers to check the two halves if they are palindromes
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True
