class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue

            if r == len(grid) - 1 and c == len(grid) - 1:
                return t

            visit.add((r, c))

            for dr, dc in dirs:
                rDiff = r + dr
                cDiff = c + dc
                if (rDiff < 0 or rDiff == len(grid) or
                    cDiff < 0 or cDiff == len(grid) or
                    (rDiff, cDiff) in visit
                ):
                    continue
                
                heapq.heappush(minH, [max(t, grid[rDiff][cDiff]), rDiff, cDiff])