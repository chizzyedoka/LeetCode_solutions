# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        def dfs(node,cur_sum,cur_path,all_paths):
            if not node:
                return 
            cur_path.append(node.val)
            if not node.left and not node.right and node.val==cur_sum:
                all_paths.append(cur_path[:])
            else:
                dfs(node.left, cur_sum-node.val, cur_path, all_paths)
                dfs(node.right, cur_sum-node.val, cur_path, all_paths)
            cur_path.pop()
        dfs(root,targetSum,[], all_paths)
        return all_paths
    
    # iterative solution
#      def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#             if not root:
#                 return []
#             stack = [root]
#             sum_stack = [root.val]
#             res = []
#             path = []
#             while stack:
#                 node = stack.pop()
#                 _sum = sum_stack.pop()
#                 if not node.left and not node.right and targetSum==_sum:
#                     # do something
#                 if node.right:
#                     stack.append(node.right)
#                     sum_stack.append(node.right.val++sum)
#                     path.append(node.val)
#                 if node.left:
#                     stack.append(node.left)
#                     sum_stack.append(node.left.val+_sum)
#                     path.append(node.val)
#             return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         self.output = []
        
#         def dfs(node,path,curSum):
#             if not root:
#                 return []
#             curSum += node.val
#             temp = path + [node.val]
#             if node.left:
#                 dfs(node.left,temp,curSum)
#             if node.right:
#                 dfs(node.right,temp,curSum)
#             if not node.left and not node.right and curSum == targetSum:
#                     self.output.append(temp)
#         dfs(root,[],0)
#         return self.output
        
        
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

        