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

        minH = [[0, 0]]
        visit = set()
        res = 0
        while len(visit) < N:
            d1, p1 = heapq.heappop(minH)
            if p1 in visit:
                continue
            visit.add(p1)
            res += d1

            for d2, p2 in adj[p1]:
                #if p2 not in visit:
                heapq.heappush(minH, [d2, p2])
        
        return res