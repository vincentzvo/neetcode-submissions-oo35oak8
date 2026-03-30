class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            minHeap.append([d, p])
        heapq.heapify(minHeap)

        res = []
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        return res