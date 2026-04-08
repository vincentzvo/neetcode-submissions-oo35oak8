class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        fresh = 0
        minutes = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append((x, y))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    adjX, adjY = x + dx, y + dy

                    if (adjX < 0 or adjX == ROWS or
                        adjY < 0 or adjY == COLS or
                        grid[adjX][adjY] != 1):
                        continue
                    
                    grid[adjX][adjY] = 2
                    q.append((adjX, adjY))
                    fresh -= 1
            
            minutes += 1
        return minutes if fresh == 0 else -1