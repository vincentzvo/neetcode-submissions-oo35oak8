class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])          # init grid limits
        pac, atl = set(), set()                             # init set for each ocean

        def dfs(r, c, visit, prevHeight):                   # define recursive dfs func with params: row, col, ocean set, height
            if ((r, c) in visit or                              # check that cell is valid and can flow into prev cell
                r < 0 or c < 0 or                                   # if not: return
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return
            visit.add((r, c))                                   # add cell to argued visit set
            dfs(r - 1, c, visit, heights[r][c])                 # call dfs on adjacent cells
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
                                                            
        for c in range(COLS):                               # call dfs on each cell in first and last row
            dfs(0, c, pac, heights[0][c])                   # dfs call on first row to pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])     # dfs on last row to atlantic

        for r in range(ROWS):                               # call dfs on each cell in first and last column
            dfs(r, 0, pac, heights[r][0])                   # dfs call on first col to pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])     # dfs call on last col to atlantic
        
        res = []                                            # init res array
        for r in range(ROWS):                               # traverse each cell
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:             # if cell in both pacific and atlantic set
                    res.append([r, c])                              # add cell to res array

        return res                                          # return res