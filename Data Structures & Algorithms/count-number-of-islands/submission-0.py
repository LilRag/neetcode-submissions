class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0 

        def dfs(r,c): 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return 

            directions = [(-1,0),(1,0), (0,1), (0,-1)]
            grid[r][c] = "0"

            for dr,dc in directions:
                nr = dr + r 
                nc = dc + c
                dfs(nr,nc)
            return 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1": 
                    island_count += 1 
                    # pass the location to the dfs function
                    dfs(row,col)

        return island_count
