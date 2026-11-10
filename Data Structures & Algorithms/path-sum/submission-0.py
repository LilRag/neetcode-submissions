# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # root 
        # target sum 
        # -15 -> 20 -> 15 -> -5 
        # do we calculate the sum of all paths and return the one that hits targetsum? 
        #otherwise how do we know which path is good 
        # some greedy approach where we see that this path is closer to the outcome , doesnt work cause negative 


        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val 
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

        