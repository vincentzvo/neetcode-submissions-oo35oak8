class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        def dfs(x, y):
            if (x < 0 or y < 0 or
                x >= ROWS or y >= COLS or
                (x, y) in visit or
                grid[x][y] == 0):
                return 0
            
            visit.add((x, y))
            return (1 + dfs(x + 1, y) +
                        dfs(x - 1, y) +
                        dfs(x, y + 1) +
                        dfs(x, y - 1))
        
        area = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    area = max(area, dfs(x, y))
        return area