# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)
        while q:
            currLevel = []
            levelSize = len(q)
            for _ in range(levelSize):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            result.append(currLevel)
        return result