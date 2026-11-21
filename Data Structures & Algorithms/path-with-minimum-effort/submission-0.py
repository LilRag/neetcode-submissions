class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # heights 2d array 
        # represents height of cell:  row , col 
        # we are situated top left 0,0 
        # we have to move down to the bottom right cell 
        # find a route that requires minimum effort 
        # can move left right up and down 
        # effort is abs(curr - next)
        # dijikstra with min heap 
        # keep a 2d scoreboard for the effort 

        import heapq

        min_heap = []

        directions = ((1,0),(-1,0),(0,1),(0,-1))


        rows = len(heights)
        cols = len(heights[0])

        effort = [[float('inf')]*cols for _ in range(rows)]
        effort[0][0] = 0 


        heapq.heappush(min_heap , (0,0,0))

        while min_heap:
            curr_effort , r, c = heapq.heappop(min_heap)
            if curr_effort > effort[r][c]:
                continue 

            if r == rows-1 and c == cols -1:
                return curr_effort 

            for dr,dc in directions:
                nr = dr + r 
                nc = dc + c 
                if 0<= nr < rows and 0 <= nc < cols:
                
                    diff = abs(heights[nr][nc] - heights[r][c])

                    new_effort = max(curr_effort, diff)
                    if new_effort  < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))

