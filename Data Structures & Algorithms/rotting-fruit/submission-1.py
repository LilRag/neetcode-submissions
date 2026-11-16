class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 empty,  1 fresh,  2 rotten fruit 
        # bfs traversal 
        # start from rotten fruits 
        # if theres a fresh fruit near it as neighbour , we convert them to rotten, and add them to queue  
        # we also keep a count of the fresh fruit, when one fruit is converted , we reduce the count 
        # in the end if the fresh count is 0, that means we got all fruits , in the queue , we keep a time count , that gets incremented 
        # if count of fresh is not 0 then we just return -1 

        from collections import deque 

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh_count = 0  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: 
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    fresh_count += 1 

        directions = ((1,0), (-1,0), (0,1), (0,-1))

        r,c,t = -1,-1,0

        while queue:
            r,c,t = queue.popleft()

            for dr, dc in directions:
                nr = dr + r 
                nc = dc + c 

                if 0<= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    queue.append((nr,nc,t+1))
                    grid[nr][nc] = 2 
                    fresh_count -= 1 
        
        return t if fresh_count ==0 else -1 




