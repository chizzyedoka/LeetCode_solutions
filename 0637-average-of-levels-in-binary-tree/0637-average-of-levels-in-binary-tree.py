# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            level_size = len(q)
            #level = []
            _sum = 0
            for _ in range(level_size):
                node = q.popleft()
                #level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                _sum += node.val
            res.append(_sum/level_size)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        # result = []
        # if not root:
        #     return result
        # q = deque()
        # q.append(root)
        # average = 0
        # while len(q)>0:
        #     currLevel = []
        #     levelSize = len(q)
        #     for _ in range(levelSize):
        #         currNode = q.popleft()
        #         if currNode.left:
        #             q.append(currNode.left)
        #         if currNode.right:
        #             q.append(currNode.right)
        #         currLevel.append(currNode.val)
        #     result.append(sum(currLevel)/levelSize)
        # return result