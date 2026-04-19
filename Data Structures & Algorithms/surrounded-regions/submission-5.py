class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])  # init rows and cols

        def dfs(r, c):                          # def recursive func with r, c params
            if (r < 0 or r == ROWS or               # base case:
                c < 0 or c == COLS or               # if r or c out of bounds or
                board[r][c] != "O"                  # cell not "O":
            ):             
                return                                  # return
            
            board[r][c] = "T"                       # set cell to temp
            dfs(r - 1, c)                           # run dfs on adjacent cells
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(ROWS):                   # traverse every row of first and last col:
            if board[r][0] == "O":                  # if cell is "O":
                dfs(r, 0)                               # run dfs
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for c in range(COLS):                   # traverse every col of first and last row:
            if board[0][c] == "O":                  # if cell is "O":
                dfs(0, c)                               # run dfs
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):                   # traverse every cell:
            for c in range(COLS):       
                if board[r][c] == "O":              # if cell is "O":
                    board[r][c] = "X"                   # set cell to "X"
                elif board[r][c] == "T":            # if cell is temp:
                    board[r][c] = "O"                   # set cell to "O"
