class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # init row and col vars
        path = set()                            # init path set

        def dfs(r, c, i):                       # revurs func with params: row, col, letter number
            if i == len(word):                  # if last letter return true
                return True                 
            if (r < 0 or c < 0 or               # return false:
                r >= ROWS or c >= COLS or       # if r or c out of bounds
                word[i] != board[r][c] or       # if cur board letter doesn't match cur word letter
                (r,c) in path):                 # if index already in path
                return False
            
            path.add((r, c))                    # add cur row,col to path
            res = (dfs(r + 1, c, i + 1) or      # set res to true if any of the surrounding idxs are valid
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))                 # remove cur row,col from path
            return res                          # return res
        
        for r in range(ROWS):                   # brute force traverse board for first letter
            for c in range(COLS):
                if dfs(r, c, 0):                # call recurs func 
                    return True
        return False
