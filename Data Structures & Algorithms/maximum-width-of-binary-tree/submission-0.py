# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # heap style indexing 
        # root i , 2i left , 2i + 1 
        # width = ilast - ifirst + 1 

        if not root:
            return 0 
            
        max_width = 0 
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            _, first_index = queue[0]

            last_index = first_index 
            for _ in range(level_size):
                node, curr_index = queue.popleft()
                curr_index -= first_index 
                last_index = curr_index 

                if node.left:
                    queue.append((node.left, 2*curr_index))
                if node.right:
                    queue.append((node.right, 2*curr_index + 1))
            
            level_width = last_index + 1 
            max_width = max(max_width, level_width)
        
        return max_width 