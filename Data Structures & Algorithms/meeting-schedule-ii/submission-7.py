"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])    # init sorted list of start times
        end = sorted([i.end for i in intervals])        # init sorted list of end times
        s = e = count = res = 0                         # init start and end ptrs, and count and res to 0

        while s < len(start):                           # loop until start ptr reaches end of start list:
            if start[s] < end[e]:                           # if cur start is less than cur end:
                s += 1                                          # increm start ptr
                count += 1                                      # increm count
            else:                                           # else (if cur start >= cur end):
                e += 1                                          # increm end ptr
                count -= 1                                      # decrem count
            res = max(res, count)                           # update res to max of cur val and count

        return res                                      # return res
    