class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if self.left and num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        heapLenDiff = len(self.left) - len(self.right)
        if abs(heapLenDiff) > 1:
            if heapLenDiff > 0:
                heapq.heappush(self.right, -heapq.heappop(self.left))
            elif heapLenDiff < 0:
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        