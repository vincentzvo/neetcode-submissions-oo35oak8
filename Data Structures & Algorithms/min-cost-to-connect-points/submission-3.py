class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)                                     # init constant for num points
        adj = defaultdict(list)                             # init adj list
        for i in range(N):                                  # traverse every point
            x1, y1 = points[i]                                  # store x and y of cur point
            for j in range(i + 1, N):                           # traverse every point idxed > cur pt
                x2, y2 = points[j]                                  # store 2nd points x and y
                dist = abs(x1 - x2) + abs(y1 - y2)                  # calc and store dist of points
                adj[i].append([dist, j])                            # populate adj list for both pts
                adj[j].append([dist, i])                            # w/ pair of dist and other point

        res = 0                                             # init res var to 0
        visit = set()                                       # init visit set
        minH = [[0, 0]]                                     # init min heap w/ pair of 0, 0
        while len(visit) < N:                               # loop while not all pts visited
            cost, i = heapq.heappop(minH)                       # store cost and cur pt from popping min heap
            if i in visit:                                      # if cur pt already visited
                continue                                            # skip pt
            res += cost                                         # add cur cost to res
            visit.add(i)                                        # add cur pt to visit set
            for neiCost, nei in adj[i]:                         # traverse each neighbor in cur pts adj list
                if nei not in visit:                                # if cur neighbor not yet visited
                    heapq.heappush(minH, [neiCost, nei])                # push cur nei cost and nei to min heap
        return res                                          # return res