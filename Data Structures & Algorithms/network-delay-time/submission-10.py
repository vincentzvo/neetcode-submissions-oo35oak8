class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for v, u, w in times:
            edges[v].append((u, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            visit.add(v1)
            t = w1

            for v2, w2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, v2))

        return t if len(visit) == n else -1