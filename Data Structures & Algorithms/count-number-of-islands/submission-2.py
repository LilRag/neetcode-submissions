class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start at the first island 
        # keep a count of the islands 
        # move in all four directions 
        # replace the current island as zero 
        # as we find another land , we add it to the queue 
        # if we are no longer able to traverse in any direction we say that is an island and increment the count 
        from collections import deque


        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        queue = deque()
        count_island = 0 

        def bfs(queue):
            
            while queue:
                r, c = queue.popleft()

                for dr , dc in directions:
                    nr = dr + r
                    nc = dc + c 

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"
            return 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue.append((i,j))
                    grid[i][j] = "0"
                    count_island += 1 
                    bfs(queue)
        return count_island


        
