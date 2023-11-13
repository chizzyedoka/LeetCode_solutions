# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = []
        if root:
            q.append(root)
        while len(q) > 0:
            currLevel = []
            for i in range(len(q)):
                curr = q.pop(0)
                currLevel.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(currLevel)
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result = []
        # if not root:
        #     return result
        # q = deque()
        # q.append(root)
        # while q:
        #     currLevel = []
        #     levelSize = len(q)
        #     for _ in range(levelSize):
        #         currNode = q.popleft()
        #         currLevel.append(currNode.val)
        #         if currNode.left:
        #             q.append(currNode.left)
        #         if currNode.right:
        #             q.append(currNode.right)
        #     result.append(currLevel)
        # return result