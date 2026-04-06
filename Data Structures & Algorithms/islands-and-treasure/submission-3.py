class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])    # init grid bounds

        def dfs(x, y, d):                       # def recursive dfs func with x, y, and distance as params
            if (x < 0 or y < 0 or                   # base case:
                x >= ROWS or y >= COLS              # if x or y out of bounds or
                or grid[x][y] == -1 or                  # square is water or
                d > grid[x][y]):                        # shorter path already found:
                return                                  # return

            grid[x][y] = min(grid[x][y], d)         # update square if new distance is min

            dfs(x + 1, y, d + 1)                    # call dfs on all adjacent squares with +1 distance
            dfs(x - 1, y, d + 1)
            dfs(x, y + 1, d + 1)
            dfs(x, y - 1, d + 1)
        
        for x in range(ROWS):                   # for each row:
            for y in range(COLS):                   # for each col:
                if grid[x][y] == 0:                     # if square is treasure chest:
                    dfs(x + 1, y, 1)                        # call dfs on all adjacent squares with 1 distance
                    dfs(x - 1, y, 1)
                    dfs(x, y + 1, 1)
                    dfs(x, y - 1, 1)