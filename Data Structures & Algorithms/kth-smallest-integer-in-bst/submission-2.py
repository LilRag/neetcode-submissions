# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in binary subtree 
        # left side contains less than node's key
        # right side contains greater than node's key 
        # kth smallest
        # we keep a count variable , and visit the left subtree
        # increment count until we have scanned through k elements 
        # inorder traversal as left < middle < right 

        stack = []
        curr = root

        while curr or stack:
            # go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # process
            curr = stack.pop()
            k -= 1 
            if k == 0:
                return curr.val

            curr = curr.right 