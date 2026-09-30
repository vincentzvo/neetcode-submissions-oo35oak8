class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for v, u, w in times:
            adj[v].append((u, w))

        minH = [(0, k)]
        visit = set()
        t = 0

        while minH:
            w1, v1 = heapq.heappop(minH)
            if v1 in visit:
                continue
            visit.add(v1)
            t = w1

            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minH, (w1 + w2, v2))

        return t if len(visit) == n else -1