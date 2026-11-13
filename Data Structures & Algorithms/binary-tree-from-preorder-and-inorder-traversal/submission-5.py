# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            #so im thinking when two arrays as provided of the tree in each of the traversal methods
            # pre order is root , left and right
            # [1,2,3,4]
            # we can say 1 is the root
            # 2 is left
            # but we cant tell where 3 and 4 lie in the tree
            # for inorder
            # left root right
            # [2,1,3,4]
            # from this we know that how much is on the left side
            # only 2 , so 3 and 4 must be on the right side cause theyre after root
            # [3,4] is preorder , after 3 we must do the left node , but since its not there we did right
            # this is provided by inorder [3,4] as 3 is root now , and after that is the right node     meaning     #there was no left node before 3 

            # pre order tells us our roots [1,2,3,4] queue of roots 
            # inorder is our map [2,1,3,4]
            # hashmap for inorder store {value:index} to find roots position 
            # pointers instead of array slicing: pass start/end indices rather than slicing arrays
            
            inorder_map = {val: idx for idx, val in enumerate(inorder)}
            pre_idx = 0 

            def build(left_bound: int, right_bound: int):
                nonlocal pre_idx

                # base case , if there are no elements to construct the subtree 
                if left_bound > right_bound:
                    return None 

                # 1 pick the current root from preorder and advance the pointer 
                root_val = preorder[pre_idx]
                pre_idx += 1 
                root = TreeNode(root_val)
                mid = inorder_map[root_val]
                root.left = build(left_bound, mid -1)
                root.right = build(mid + 1, right_bound)

                return root 

            return build(0, len(inorder) - 1)
