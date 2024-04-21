# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result = deque()
        # if not root:
        #     return result
        # q = deque()
        # q.append(root)
        # while q:
        #     curLevel = []
        #     levelSize = len(q)
        #     for _ in range(levelSize):
        #         currNode = q.popleft()
        #         curLevel.append(currNode.val)
        #         if currNode.left:
        #             q.append(currNode.left)
        #         if currNode.right:
        #             q.append(currNode.right)
        #     result.appendleft(curLevel)
        # return result
            