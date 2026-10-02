class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)                               # init const var for grid max
        visit = set((0, 0))                         # init visit set with top left cell
        minH = [[grid[0][0], 0, 0]]                 # init min heap to hold max cell val, row, col w/ top left cell
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]   # init directions for adj cells

        while minH:                                 # loop until min heap empty
            t, r, c = heapq.heappop(minH)               # pop and store time, row, col from min heap

            if r == N - 1 and c == N - 1:               # if cur cell bottom right
                return t                                    # return time
            
            for dr, dc in dirs:                         # traverse directions storing row and coll diffs
                neiR, neiC = r + dr, c + dc                 # update neighbor row and col according to diffs
                if (neiR < 0 or neiR == N or                # if cur neighbor cell out of bounds or visited
                    neiC < 0 or neiC == N or                    # continue
                    (neiR, neiC) in visit
                ):
                    continue
                
                visit.add((neiR, neiC))                                         # add neigbor cell to visit
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])    # push neigbor cell to min heap
                                                                                # with max of cur t and cur cell val