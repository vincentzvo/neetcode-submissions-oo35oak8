class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, x, y = heapq.heappop(minH)

            if (x, y) in visit:
                continue

            if x == len(grid) - 1 and y == len(grid) - 1:
                return t

            visit.add((x, y))

            for xDif, yDif in dirs:
                x1, y1 = x + xDif, y + yDif

                if (x1 < 0 or x1 == len(grid) or
                    y1 < 0 or y1 == len(grid) or
                    (x1, y1) in visit
                ):
                    continue

                heapq.heappush(minH, [max(t, grid[x1][y1]), x1, y1])
            