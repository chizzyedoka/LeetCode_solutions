"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        stack = []
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                    cur.next.prev = None
                    
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None

            if cur.next:
                cur = cur.next
            else:
                break

        while stack:
            node = stack.pop()
            cur.next = node
            node.prev = cur
            while cur.next:
                cur = cur.next

        return head