class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]
        prevEnd = res[-1][1]

        for start, end in intervals[1:]:

            if start >= prevEnd:
                res.append([start, end])
                prevEnd = end
                continue

            prevEnd = min(prevEnd, end)

        return len(intervals) - len(res)