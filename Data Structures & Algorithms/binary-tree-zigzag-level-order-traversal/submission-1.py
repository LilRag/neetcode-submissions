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
            if len(res) % 2:
                curr_level.reverse()
            res.append(curr_level)
        return res 