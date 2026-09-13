class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: 
                    queue.append((row,col))

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions: 
                nr = dr + r
                nc = dc + c 

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1 
                    queue.append((nr,nc))

        return 
