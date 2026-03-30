class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        numsLen = len(self.nums)
        if numsLen % 2:
            print(numsLen)
            return self.nums[numsLen // 2] #if numsLen > 1 else self.nums[0]
        else:
            print(numsLen)
            print(numsLen / 2)
            return (self.nums[numsLen // 2] + self.nums[(numsLen // 2) - 1]) / 2