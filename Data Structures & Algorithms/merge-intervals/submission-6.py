class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                            # sort given intervals list in place
        res = [intervals[0]]                        # init res list with first given interval in it

        for start, end in intervals[1:]:            # traverse intervals (skipping first) and tracking start and end pair vals:
            prevEnd = res[-1][1]                        # set/update prevEnd to 2nd val in last interval in res list

            if start <= prevEnd:                        # if cur interval overlaps w/ prev interval (cur start <= prev end):
                res[-1][1] = max(prevEnd, end)              # update prev intervals end val to max of the w intervals
            else:                                       # else (if intervals don't overlap):
                res.append([start, end])                    # append cur interval to res list
        
        return res                                  # return res list