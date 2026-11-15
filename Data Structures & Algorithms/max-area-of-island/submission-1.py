class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        from collections import deque 

        rows = len(grid)
        cols = len(grid[0])

        max_area = 0 
        queue = deque()

        directions = ((1,0), (-1,0) , (0,1), (0,-1))
        
        def bfs(queue):
            nonlocal curr_area 
            while queue:
                r,c = queue.popleft()              
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c  
                    
                    if 0<= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        curr_area += 1 
                        grid[nr][nc] = 0 

            return 

        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 1:
                    curr_area = 1 
                    queue.append((i,j))
                    grid[i][j] = 0
                    bfs(queue)
                    
                    max_area = max(max_area, curr_area)

        return max_area
