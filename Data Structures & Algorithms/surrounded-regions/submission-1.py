class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque 


        rows = len(board)
        cols = len(board[0])


        queue = deque()
        # top and bottom 
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "S"
                queue.append((0,c))
            
            if board[rows-1][c] =="O":
                board[rows-1][c] = "S"
                queue.append((rows-1,c))

        for r in range(rows):

            if board[r][0] == "O":
                board[r][0] ="S"
                queue.append((r,0))

            if board[r][cols-1] == "O":
                board[r][cols-1] ="S"
                queue.append((r,cols-1))


        directions = ((1,0),(-1,0),(0,1),(0,-1))

        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc 

                if 0<= nr < rows and 0<= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    queue.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "S":
                    board[r][c] = "O"


