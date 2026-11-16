class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # rectangular island heights where heights[r][c] show height above sea level 
    # pacific ocean top and left ; r = 0 and c =0  
    # atlantic ocean bottom and right: r = rows - 1 and c = cols - 1 
    # im taking it as a minecraft bucket , dropped on a hill , it flows to the cells that are at equal or lower height 
    # what if we switch it, go from the other way from ocean to cells, if the cell is lesser than the previous cell water flows through them 
    # then we find common cells from both pacific and atlantic 
    # climbing from ocean -> next_height >= curr_height 

    # two sets pacific reachable and atlantic reachab;e 
    # two bfs queues, one that starts for pacific and one for atlantic based on the indexes 
    # add all starts to visited and queue , then start the while queue 
    # in the while queue, for each neighbour within bounds and not in visited check the condition 
    # mark visited and push to queue 
    # return the intersection of both 
        rows = len(heights)
        cols = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def bfs(queue, ocean_set):
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            while queue:
                r,c = queue.popleft()

                for dr , dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in ocean_set and  heights[nr][nc] >= heights[r][c]:
                        ocean_set.add((nr,nc))
                        queue.append((nr,nc))
            
            
            return ocean_set
                    


        # top row and bottom row  
        for c in range(cols):
            pacific_set.add((0,c))
            atlantic_set.add((rows-1,c))

        # left row and right row
        for r in range(rows):
            pacific_set.add((r,0))
            atlantic_set.add((r,cols-1))

        pacific_queue = deque(pacific_set)
        atlantic_queue = deque(atlantic_set)
        
        pacific_reachable = bfs(pacific_queue, pacific_set)
        atlantic_reachable = bfs(atlantic_queue, atlantic_set)

        return [[r,c] for r,c in (pacific_reachable & atlantic_reachable)]
