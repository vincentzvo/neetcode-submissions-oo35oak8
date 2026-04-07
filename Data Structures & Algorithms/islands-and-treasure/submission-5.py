class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])    # init rows and cols
        visit = set()                           # init visit set
        q = deque()                             # init queue

        def addGrid(r, c):                      # def helper function to not traverse invalid squares
            if (r < 0 or r == ROWS or               # base case:
                c < 0 or c == COLS or               # if row or col out of bounds or
                (r, c) in visit or                      # r, c in visit set or
                grid[r][c] == -1):                      # square is water
                return                                  # return without adding square to queue
            
            visit.add((r, c))                       # add square r, c to visit set
            q.append([r, c])                        # append square r, c to queue

        for r in range(ROWS):                   # for each row:
            for c in range(COLS):                   # for each col:
                if grid[r][c] == 0:                     # if square is treasure chest
                    q.append([r, c])                        # append square r, c to queue
                    visit.add((r, c))                       # add square r, c to visit set
        
        dist = 0                                # init distance to 0
        while q:                                # while queue is not empty
            for i in range(len(q)):                 # for each square in queue:
                r, c = q.popleft()                      # set r, c to q popleft
                grid[r][c] = dist                       # set square r, c to dist

                addGrid(r + 1, c)                       # call helper on each adjacent square
                addGrid(r - 1, c)
                addGrid(r, c + 1)
                addGrid(r, c - 1)

            dist += 1                               # increment distance