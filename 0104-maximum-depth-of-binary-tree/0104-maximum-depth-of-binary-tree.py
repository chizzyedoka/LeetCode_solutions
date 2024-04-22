# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs iterative solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        res = 1
        while stack:
            node,depth = stack.pop()
            if node:
                res = max(depth,res)    
                stack.append((node.right,depth+1))
                stack.append((node.left,depth+1))
        return res
    
    
    # bfs iterative solution
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         count = 0
#         if not root:
#             return count
#         q = deque()
#         q.append(root)
#         while q:
#             level_size = len(q)
#             count += 1
#             for _ in range(level_size):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return count
            
        
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     maxRight = self.maxDepth(root.right)
    #     maxLeft = self.maxDepth(root.left)
    #     return 1 + max(maxLeft,maxRight)
        
        
        
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     def dfs(root,count=0):
    #         if not root: return count
    #         if root.left: dfs(root.left,count+1)
    #         if root.right: dfs(root.right,count+1)
    #     return  dfs(dfs,count) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root: # no root
        #     return 0
        # else:
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
        