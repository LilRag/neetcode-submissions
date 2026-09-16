# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def checkheight(node):
            nonlocal isBalanced
            if node is None:
                return 0

            left_h =checkheight(node.left)
            right_h =checkheight(node.right)


            if abs(left_h - right_h) > 1:
                isBalanced = False
            return 1 + max(left_h, right_h)

        checkheight(root)
        return isBalanced