class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append((x, y))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q and fresh:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    if (x + dx < 0 or x + dx == ROWS or
                        y + dy < 0 or y + dy == COLS or
                        grid[x + dx][y + dy] != 1):
                        continue
                    
                    grid[x + dx][y + dy] = 2
                    fresh -= 1
                    q.append((x + dx, y + dy))   
            time += 1
        return time if not fresh else -1