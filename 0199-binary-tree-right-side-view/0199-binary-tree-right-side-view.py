# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        q=deque()
        q.append(root)
        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if _==level_size-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root: return []
        # queue = [root]
        # result = []
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     result.append(node.val)
        # return result