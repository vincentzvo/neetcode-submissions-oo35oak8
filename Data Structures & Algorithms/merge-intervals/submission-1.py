class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        curInterval = intervals.pop(0)
        res = []

        for i in range(len(intervals)):
            if curInterval[1] < intervals[i][0]:
                res.append(curInterval)
                curInterval = intervals[i]
            elif curInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                curInterval = [min(curInterval[0], intervals[i][0]),
                               max(curInterval[1], intervals[i][1])]
        
        res.append(curInterval)
        return res