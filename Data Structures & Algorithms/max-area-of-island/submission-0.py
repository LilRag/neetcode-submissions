class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0 
        max_area = 0 


        def dfs(r,c): 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            directions = [(-1,0),(1,0), (0,1), (0,-1)]
            grid[r][c] = 0
            area = 1 


            for dr,dc in directions:
                nr = dr + r 
                nc = dc + c
                area += dfs(nr,nc)

            return area  

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    island_count += 1 
                    # pass the location to the dfs function 
                    area = dfs(row,col)
                    max_area = max(max_area,area)

                    
        return max_area