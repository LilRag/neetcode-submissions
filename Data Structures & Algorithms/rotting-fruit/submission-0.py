class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh_count = 0 
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,0)) # (row,col,minutes)
                elif grid[row][col] == 1:
                    fresh_count += 1 

        if fresh_count == 0:
            return 0 

        while queue:
            r,c,m = queue.popleft()
            for dr,dc in directions:
                nr = dr + r 
                nc = dc + c 

                if 0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1 
                    queue.append((nr,nc,m +1))
        
        if fresh_count > 0:
            return -1 

        else:
            return m

        
