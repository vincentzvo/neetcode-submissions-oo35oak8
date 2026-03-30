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
            print("len diff triggered")
            if heapLenDiff > 0:
                heapq.heappush(self.right, -heapq.heappop(self.left))
            elif heapLenDiff < 0:
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        print(self.left)
        print(self.right)
        if len(self.left) == len(self.right):
            print("calc")
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            print("L")
            return -self.left[0]
        else:
            print("R")
            return self.right[0]
        