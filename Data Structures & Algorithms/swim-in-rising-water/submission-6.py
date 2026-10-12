class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        res = 0

        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            visit.add((r, c))

            res = max(res, t)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return res

            for dr, dc in dirs:
                rDiff = r + dr
                cDiff = c + dc
                if (rDiff < 0 or rDiff == len(grid) or
                    cDiff < 0 or cDiff == len(grid) or
                    (rDiff, cDiff) in visit
                ):
                    continue
                
                heapq.heappush(minH, [grid[rDiff][cDiff], rDiff, cDiff])