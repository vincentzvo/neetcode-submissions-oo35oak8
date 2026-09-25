class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)                               # init adjList hashmap of node edges
        for u, v, w in times:                                   # traverse node edges
            edges[u].append((v, w))                                 # populate edge list

        minHeap = [(0, k)]                                      # init minHeap with (0 weight, start node)
        visit = set()                                           # init set of visited nodes
        t = 0                                                   # init time var to 0
        while minHeap:                                          # loop until minHeap is empty
            w1, n1 = heapq.heappop(minHeap)                         # pop from minHeap and assign weight and next node to vars
            if n1 in visit:                                         # if next node already visited:
                continue                                                # continue
            visit.add(n1)                                           # add next node to visit set
            t = w1                                                  # update time to cur node weight

            for n2, w2 in edges[n1]:                                # traverse neighbors of cur node
                if n2 not in visit:                                     # if cur neigbor node not yet visited
                    heapq.heappush(minHeap, (w1 + w2, n2))                  # push tuple of cur + neighbor weight and neighbor to minHeap

        return t if len(visit) == n else -1                     # return time if all nodes visited and -1 if not