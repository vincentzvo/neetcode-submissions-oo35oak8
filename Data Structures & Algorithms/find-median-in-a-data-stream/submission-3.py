class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        heapLenDif = len(self.minHeap) - len(self.maxHeap)
        if abs(heapLenDif) > 1:
            if heapLenDif > 0:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        heapLenDif = len(self.minHeap) - len(self.maxHeap)
        if heapLenDif > 0:
            return self.minHeap[0]
        elif heapLenDif < 0:
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2