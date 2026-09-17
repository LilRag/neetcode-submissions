"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_uniform(r,c,length):
            first_val = grid[r][c]
            for i in range(r, r+length):
                for j in range(c, c+length):
                    if grid[i][j] != first_val:
                        return False

            return True

        def build (r,c,length):
            if is_uniform(r,c,length):
                return Node(val = bool(grid[r][c]), isLeaf=True)

            half = length // 2

            top_left = build(r,c,half)
            top_right = build(r,c+half, half)
            bottom_left = build(r + half, c, half)
            bottom_right = build(r + half, c + half, half)

            return Node(
                val=True, # Value doesn't matter when isLeaf is False
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
            )

        return build(0, 0, len(grid))