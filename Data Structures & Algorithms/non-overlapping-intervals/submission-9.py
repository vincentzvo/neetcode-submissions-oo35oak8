class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()                        # sort given intervals list in place
        res = 0                                 # init res count to 0
        prevEnd = intervals[0][1]               # init prevEnd as end of first interval

        for start, end in intervals[1:]:        # traverse intervals (skipping first) gathering start and end vals
            if start >= prevEnd:                    # if cur and prev intervals don't overlap (cur start >= prev end)
                prevEnd = end                           # update prevEnd to cur intervals end
            else:                                   # else (if cur interval overlaps with prev):
                prevEnd = min(prevEnd, end)             # update prevEnd to min of prev and cur intervals end
                res += 1                                # increment res count var

        return res                              # return res