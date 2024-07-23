# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        _sum = 0
        order = []
        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                order.append(node.val)
                if node.val >= low and node.val <= high:
                    _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print(order)
        return _sum