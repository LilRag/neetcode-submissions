class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque 

        number_of_islands = 0 

        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque() 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    queue.append((row,col))
                    grid[row][col] = "0"
                    number_of_islands += 1

                    while queue: 
                        r, c = queue.popleft()
                        
                        for dr, dc in directions:
                            nr = r + dr 
                            nc = c + dc 
                            if  nr >= 0  and nr < rows and nc >= 0  and nc < cols and grid[nr][nc] == "1":
                                queue.append((nr,nc)) 
                                grid[nr][nc] = "0"
                
    
        return number_of_islands
