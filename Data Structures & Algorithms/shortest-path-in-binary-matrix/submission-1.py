class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Early exit if start or destination is blocked
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        # Directions ordered greedily toward bottom-right (n-1, n-1)
        directions = [
            (1, 1),   # Down-Right (primary diagonal)
            (1, 0),   # Down
            (0, 1),   # Right
            (1, -1),  # Down-Left
            (-1, 1),  # Up-Right
            (0, -1),  # Left
            (-1, 0),  # Up
            (-1, -1)  # Up-Left
        ]
        
        min_len = float('inf')
        
        def dfs(r: int, c: int, path_len: int) -> None:
            nonlocal min_len
            
            # Pruning: if current path is already >= best found so far, stop early
            if path_len >= min_len:
                return
            
            # Reached destination
            if r == n - 1 and c == n - 1:
                min_len = min(min_len, path_len)
                return
            
            # Mark current cell as visited for this path
            grid[r][c] = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    dfs(nr, nc, path_len + 1)
            
            # Backtrack: unmark cell so other paths can explore it
            grid[r][c] = 0
        
        dfs(0, 0, 1)
        return min_len if min_len != float('inf') else -1