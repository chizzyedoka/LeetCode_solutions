# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS approach
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        def dfs(node):
            if not node:
                return 0
    
            if low <= node.val <= high:
                self.total += node.val
                
            if node.left and node.val > low:
                dfs(node.left)
                
            if node.right and node.val < high:
                dfs(node.right)
        
                
        dfs(root)
        return self.total
        
    
    
    # BFS approach
    # from collections import deque
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     if not root:
    #         return 0
    #     q = deque()
    #     q.append(root)
    #     _sum = 0
    #     while q:
    #         level_size = len(q)
    #         for _ in range(level_size):
    #             node = q.popleft()
    #             if low <= node.val <= high:
    #                 _sum += node.val
    #             if node.left and node.val > low:
    #                 q.append(node.left)
    #             if node.right and node.val < high:
    #                 q.append(node.right)
    #     return _sum