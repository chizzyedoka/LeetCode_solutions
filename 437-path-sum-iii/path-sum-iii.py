# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: 
        self.count = 0 
        def findSum(node, curSum): 
            if not node: 
                return 
            curSum += node.val 
            if curSum == targetSum: 
                self.count += 1 
            findSum(node.left, curSum) 
            findSum(node.right, curSum) 
        
        def dfs(node): 
            if not node: 
                return 
            findSum(node, 0) 
            dfs(node.left) 
            dfs(node.right) 
        
        dfs(root)
        return self.count