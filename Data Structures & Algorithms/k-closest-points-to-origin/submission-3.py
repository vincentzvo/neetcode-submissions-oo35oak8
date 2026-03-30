class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for x, y in points:
            d = x ** 2 + y ** 2
            heapq.heappush(minHeap, [d, x, y])
        
        res = []
        while k:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res