class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fruitCount = 0

        def addCell(x, y):
            if (x < 0 or x == ROWS or
                y < 0 or y == COLS or
                (x, y) in visited or
                grid[x][y] != 1):
                return

            q.append((x, y))
            visited.add((x, y))

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 2:
                    q.append((x, y))
                    visited.add((x, y))
                if grid[x][y] != 0:
                    fruitCount += 1
        
        firstFruit = True
        minutes = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                print((x, y))
                addCell(x + 1, y)
                addCell(x - 1, y)
                addCell(x, y + 1)
                addCell(x, y - 1)
            
            if not firstFruit: minutes += 1
            firstFruit = False
        
        return minutes if fruitCount == len(visited) else -1