# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        

        if not root:
            return 0 
        
        queue = deque([(root, root.val)])
        goodnode_count = 0 
        while queue:
            node, max_val = queue.popleft()
            
            if node.val >= max_val:
                goodnode_count += 1 
            
            new_max = max(max_val, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
        
        return goodnode_count

        