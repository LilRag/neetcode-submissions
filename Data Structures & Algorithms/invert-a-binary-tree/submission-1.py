# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # switch left and right child 
        # then traverse and repeat 
        if not root:
            return None

        node = root 

        node.left , node.right = node.right, node.left 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


        