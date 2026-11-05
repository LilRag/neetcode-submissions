# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # when even , right and left
        # when odd , left and right 
        from collections import deque 
        if not root:
            return []
        left_to_right = True 

        res = []

        queue = deque([root])

        while queue:

            level = len(queue)
            curr_level = []

            for _ in range(level):
                node = queue.popleft()
                curr_level.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            #flip the values if this level needs to be right to left
            if not left_to_right:
                curr_level.reverse()
            
            res.append(curr_level)
            left_to_right = not left_to_right

        return res 