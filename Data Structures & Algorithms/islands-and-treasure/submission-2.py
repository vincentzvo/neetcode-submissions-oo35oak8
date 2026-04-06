class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y, d):
            if (x < 0 or y < 0 or
                x >= ROWS or y >= COLS
                or grid[x][y] == -1 or
                d > grid[x][y]):
                return

            grid[x][y] = min(grid[x][y], d)

            dfs(x + 1, y, d + 1)
            dfs(x - 1, y, d + 1)
            dfs(x, y + 1, d + 1)
            dfs(x, y - 1, d + 1)
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    dfs(x + 1, y, 1)
                    dfs(x - 1, y, 1)
                    dfs(x, y + 1, 1)
                    dfs(x, y - 1, 1)