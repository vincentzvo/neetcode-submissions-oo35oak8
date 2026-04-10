class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(x, y):
            if (x < 0 or x == ROWS or
                y < 0 or y == COLS or
                (x, y) in visit or
                grid[x][y] == -1):
                return

            q.append((x, y))
            visit.add((x, y))

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    q.append((x, y))
                    visit.add((x, y))
        
        dist = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist
                addCell(x + 1, y)
                addCell(x - 1, y)
                addCell(x, y + 1)
                addCell(x, y - 1)
            
            dist += 1