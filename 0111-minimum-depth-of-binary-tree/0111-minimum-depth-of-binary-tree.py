# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        count = 0
        while q:
            count += 1
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if not node.left and not node.right:
                    return count
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                
        