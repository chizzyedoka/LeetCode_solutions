# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Helper function to reverse a linked list
        def reverse(slow):
            prev = None
            while slow:
                next_node = slow.next
                slow.next = prev
                prev = slow
                slow = next_node
            return prev
        
        if not head or not head.next:
            return True
        
        if not head.next.next:
            return head.val == head.next.val
        
        slow, fast = head, head
        # Move slow to the middle of the linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        reversed_half = reverse(slow.next)
        
        # Compare the first half and reversed half of the linked list
        cur = head
        while cur and reversed_half:
            if cur.val != reversed_half.val:
                return False
            cur = cur.next
            reversed_half = reversed_half.next
        return True

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         # helper function
#         def reverse(slow):
#             prev = None
#             while slow:
#                 next_node = slow.next
#                 slow.next = prev
#                 prev = slow
#                 slow = next_node
#             return prev
        
#         if not head or not head.next:
#             return True
        
#         if not head.next.next:
#             return head.val == head.next.val
        
#         slow,fast = head, head
#         # get slow to the middle of the LL
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
       
#         # reverse one half
#         reversed_half = reverse(slow.next)
#         slow.next = None  
        
#         # compare first_half and reversed_half
#         cur = head
#         while (reversed_half and reversed_half.next):
#             if cur.val != reversed_half.val:
#                 return False
#             cur = cur.next
#             reversed_half = reversed_half.next
#         return True
        
        
        
        
        
        
    # def isPalindrome(self, head: ListNode) -> bool:
    #     vals = []
    #     current_node = head
    #     while current_node is not None:
    #         vals.append(current_node.val)
    #         current_node = current_node.next
    #     return vals == vals[::-1]
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
            
            
        