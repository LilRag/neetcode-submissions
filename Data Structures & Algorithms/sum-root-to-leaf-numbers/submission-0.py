# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # root given 
        # for each path , we calculate the number
        # then add up all paths 

        # 1 -> 5 , 15 
        # 1 -> 1 -> 6, 116 
        # 15 + 116 = 131 

        # recursive approach 
        # dfs functon , keeping track of current path
        # base condition is us hitting a leaf node 
        # we add up all the chars and put that in the result list 

        # if not a leaf node , we traverse the left and the right path 

        # after we pop out of the current path to back track 
        res = []

        def dfs(node , current_path):

            if not node:
                return 
            
            current_path.append(node.val)
            
            if not node.left and not node.right:
                res.append(int("".join(map(str, current_path))))
            
            else:
                dfs(node.left, current_path)
                dfs(node.right, current_path)

            current_path.pop()

        dfs(root, [])
        return sum(res)

