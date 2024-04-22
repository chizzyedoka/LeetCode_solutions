# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            _sum = 0
            for _ in range(level_size):
                node = q.popleft()
                _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(_sum)
        if k > len(level_sums):
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k-1]