class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.res = 0
        self.area = 0
        visit = set()

        def dfs(x, y):
            if (x < 0 or y < 0 or
                x >= ROWS or y >= COLS or
                (x, y) in visit or
                grid[x][y] == 0):
                self.res = max(self.res, self.area)
                return

            self.area += 1
            visit.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    self.area = 0
                    dfs(x, y)

        return self.res