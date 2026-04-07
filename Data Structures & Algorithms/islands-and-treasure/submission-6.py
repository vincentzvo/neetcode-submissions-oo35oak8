class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def AddCell(x, y):
            if (x < 0 or x == ROWS or
                y < 0 or y == COLS or
                (x, y) in visit or
                grid[x][y] == -1):
                return

            visit.add((x, y))
            q.append((x, y))
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    q.append((x, y))

        dist = 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                visit.add((x, y))
                grid[x][y] = min(grid[x][y], dist)

                AddCell(x + 1, y)
                AddCell(x - 1, y)
                AddCell(x, y + 1)
                AddCell(x, y - 1)
            
            dist += 1
