class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visit = set()
        res = 0
        minH = [[0, 0]]
        while len(visit) < N:
            d, p = heapq.heappop(minH)
            if p in visit:
                continue
            visit.add(p)
            res += d
            
            for neiDist, nei in adj[p]:
                if nei not in visit:
                    heapq.heappush(minH, [neiDist, nei])
        
        return res