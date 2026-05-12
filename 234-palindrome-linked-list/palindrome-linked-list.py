# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def get_mid(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_linked_list(node): # 1-> 2 -> 3 -> 4
            prev = None
            cur = node
            while cur:
                next_node = cur.next # 3 -> 4
                cur.next = prev # 2 -> 1 -> None
                prev = cur
                cur = next_node # 2 -> 3 -> 4
            return prev

        mid_node = get_mid(head)
        reversed_mid_node = reverse_linked_list(mid_node)

        cur = reversed_mid_node
        while cur and cur.next:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        return True
