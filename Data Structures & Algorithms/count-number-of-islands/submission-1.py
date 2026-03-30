class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])    # init grid # of rows and cols
        res = 0                                 # init res

        def dfs(x, y):                          # recurs dfs func
            if (x < 0 or y < 0 or               # base case:
                x >= ROWS or y >= COLS or         # if x or y out of bounds or
                grid[x][y] == "0"):               # cur grid not island:
                return                              # return

            grid[x][y] = "0"                    # change island to 0 so it isn't considered again later
            dfs(x + 1, y)                       # run dfs on all surrounding grid spaces
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for x in range(ROWS):                   # for each row:
            for y in range(COLS):                   # for each col:
                if grid[x][y] == "1":                   # if grid space is island:
                    dfs(x, y)                               # run dfs
                    res += 1                                # increm res

        return res                              # return res