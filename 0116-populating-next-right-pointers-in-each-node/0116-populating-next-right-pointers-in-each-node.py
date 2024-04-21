"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        if not root:
            return 
        q = deque()
        q.append(root)
        while q:
            prev_node = None
            level_size = len(q)
            for _ in range(level_size):
                cur_node = q.popleft()
                if prev_node:
                    prev_node.next = cur_node
                prev_node = cur_node
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right) 
        return root
                        