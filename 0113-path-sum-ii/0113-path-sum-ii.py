# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        
        def dfs(node,path,curSum):
            if not root:
                return []
            curSum += node.val
            temp = path + [node.val]
            if node.left:
                dfs(node.left,temp,curSum)
            if node.right:
                dfs(node.right,temp,curSum)
            if not node.left and not node.right and curSum == targetSum:
                    self.output.append(temp)
        dfs(root,[],0)
        return self.output
        
        
        # output = []   
        # def dfs(root,curSum,pathList):
        #     if not root:
        #         return 
        #     curSum += root.val
        #     pathList.append(root.val)
        #     print(pathList)
        #     if not root.left and not root.right:
        #         if targetSum == curSum:
        #             output.append(pathList)
        #     if root.left:
        #         dfs(root.left,curSum,pathList)
        #     if root.right:
        #         dfs(root.right,curSum,pathList)
        #         # self.pathList.pop()
        # dfs(root,0,[])
        # return output

        