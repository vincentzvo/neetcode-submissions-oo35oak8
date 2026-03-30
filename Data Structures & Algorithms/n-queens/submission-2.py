class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()                                     # init col and diag sets
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []                                        # init res
        board = [["."] * n for i in range(n)]           # init board as n list rows of n "." cols

        def backtrack(r):                               # recurs func w/ cur row param
            if r == n:                                      # base case: if on last row + 1:
                copy = ["".join(row) for row in board]          # join every row in board
                res.append(copy)                                # append to res
                return                                          # return

            for c in range(n):                              # for each col in cur row
                if (c in col or                                 # if queen in cur col or
                    r + c in posDiag or                         # queen in either diag
                    r - c in negDiag):
                    continue                                        # continue
                
                col.add(c)                                      # add cur col to cols set
                posDiag.add(r + c)                              # add cur row + col to posDiag
                negDiag.add(r - c)                              # add cur row - col to negDiag
                board[r][c] = "Q"                               # edit board with new queen

                backtrack(r + 1)                                # cal recur on next row

                col.remove(c)                                   # remove cur col to cols set
                posDiag.remove(r + c)                           # remove cur row + col to posDiag
                negDiag.remove(r - c)                           # remove cur row - col to negDiag
                board[r][c] = "."                               # revert board to previous
        
        backtrack(0)                                    # call recurs func on first row
        return res                                      # return res