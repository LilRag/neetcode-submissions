class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,reachable_set):
            reachable_set.add((r,c))

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<= nr < rows and 0 <= nc < cols and (nr,nc) not in reachable_set and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,reachable_set)
                    
        for c in range(cols):
            dfs(0,c,pacific_reachable)
            dfs(rows-1,c,atlantic_reachable)

        for r in range(rows):
            dfs(r,0,pacific_reachable)
            dfs(r,cols-1,atlantic_reachable)

        overlap = pacific_reachable & atlantic_reachable 
        output = [[a,b] for a,b in overlap]

        return output 
