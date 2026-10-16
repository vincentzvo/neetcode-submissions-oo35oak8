class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minH = [[grid[0][0], 0, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            visit.add((r, c))

            for rDif, cDif in dirs:
                dr, dc = r + rDif, c + cDif
                if (dr < 0 or dr == N or
                    dc < 0 or dc == N or
                    (dr, dc) in visit
                ):
                    continue
                visit.add((dr, dc))
                heapq.heappush(minH, [max(t, grid[dr][dc]), dr, dc])