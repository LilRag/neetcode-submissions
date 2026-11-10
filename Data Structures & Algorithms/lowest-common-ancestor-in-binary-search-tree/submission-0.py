# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lowest common ancestor 
        # lowest node in a tree such that p and q are decendants 
        # ancestor can be a decendant itself 

        # an ancestor is a decendant of itself when it lies on the same side of the subtree as the other decendant 
        # this is a bst , so the left node < root < right node 
        # we traverse the tree from the root 
        # if we find p and q , we save the root node as its lca? 

        # recursively call this function , when we find p and q we return out until their roots are the same , that would be its lca? 


        # better approach 
        # when left node val < root node val < rightr node val 
        # divergent base condition , this becomes our lca 

        # if not left < root and right < root , we go to the left subtree 
        # vice versa for right subtree 

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left , p, q)
                        

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p , q)
        
        else:
            return root 
