class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return t
            visit.add((r, c))

            for x, y in dirs:
                dr, dc = r + x, c + y
                if (dr < 0 or dr == len(grid) or
                    dc < 0 or dc == len(grid) or
                    (dr, dc) in visit
                ):
                    continue
                    
                visit.add((dr, dc))
                heapq.heappush(minH, [max(grid[dr][dc], t), dr, dc])