# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal and keep only the last node     
        from collections import deque 

        if not root:
            return []

        queue = deque([root])

        res = []
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

            res.append(curr_level[-1])

        return res 