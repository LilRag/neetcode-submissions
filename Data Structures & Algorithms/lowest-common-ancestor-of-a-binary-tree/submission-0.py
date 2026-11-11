# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # so what im thinking is 
        # we need to use the backtracking logic of recursive dfs 
        # we find p first , then another path finds q , back track both and see which is the node that connects both together?  
        # previous approach stores the path , which is O(n)

        # let at each recursive call , we answer did we find p , q  or their lca 

        # base case 
        # if node is none return none 
        # if node == p or node == q , return node 

        # recrurse
        # left = lowest..(node.left, p , q)
        # right = lowest..(node.right, p , q)

        # both left and right are none , that means p was found in left and q was found in right 
        # the split is the lca , so it would be the current node 

        # only one side returned node, both p and q are located in the same subtree
        # return whichever side is not none 
        # both are none , neither p nor q exists in the subtree return none 


        if not root or root == p or root == q:
            return root 

        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)

        if left and right:
            return root

        return left if left else right