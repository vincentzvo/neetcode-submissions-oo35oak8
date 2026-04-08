class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])                # init ROW and COL max vals
        
        q = deque()                                         # init queue
        fresh = 0                                           # init fresh and minutes
        minutes = 0

        for x in range(ROWS):                               # traverse every cell:
            for y in range(COLS):
                if grid[x][y] == 1:                                 # if cell is fresh:
                    fresh += 1                                          # increm fresh
                if grid[x][y] == 2:                                 # if cell is rotten:
                    q.append((x, y))                                    # append cell to queue
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]     # init array of adjacent coordinates
        while q and fresh > 0:                              # loop until q is empty or no fresh fruit left
            for i in range(len(q)):                             # loop for every cell cur in queue
                x, y = q.popleft()                                  # get cur cell
                for dx, dy in directions:                           # for every adj cell:
                    adjX, adjY = x + dx, y + dy                         # calc adj cell

                    if (adjX < 0 or adjX == ROWS or                     # check validity & freshness of adj cell
                        adjY < 0 or adjY == COLS or
                        grid[adjX][adjY] != 1):
                        continue                                            # continue to next adj cell if invalid
                        
                    grid[adjX][adjY] = 2                                # set adj cell to rotten
                    q.append((adjX, adjY))                              # append adj cell to queue
                    fresh -= 1                                          # decrem # fresh fruit
            
            minutes += 1                                        # increm minutes
        return minutes if fresh == 0 else -1                # return minutes if all fruit was able to rot else return -1