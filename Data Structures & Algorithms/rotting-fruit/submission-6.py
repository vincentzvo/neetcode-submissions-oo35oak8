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
                    adjX, adjY = x + dx, y + dy
                    if (adjX < 0 or adjX == ROWS or
                        adjY < 0 or adjY == COLS or
                        grid[adjX][adjY] != 1):
                        continue
                    
                    grid[adjX][adjY] = 2
                    fresh -= 1
                    q.append((adjX, adjY))   
            time += 1
        return time if not fresh else -1