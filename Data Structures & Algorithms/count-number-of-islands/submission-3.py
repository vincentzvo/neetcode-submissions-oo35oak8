class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(x, y):
            if (x < 0 or y < 0 or
                x >= ROWS or y >= COLS or
                grid[x][y] == '0'):
                return
            
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == '1':
                    dfs(x, y)
                    res += 1

        return res