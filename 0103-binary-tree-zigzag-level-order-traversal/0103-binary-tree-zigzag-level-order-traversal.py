# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = deque()
        q.append(root)
        res = []
        switch = True
        while q:
            level = deque()
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if switch:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            switch = not switch
            res.append(level)
        return res
        