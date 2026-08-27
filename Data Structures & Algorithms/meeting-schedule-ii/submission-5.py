"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        s = e = count = res = 0

        while s < len(start) and e < len(end):
            while s < len(start) and start[s] < end[e]:
                s += 1
                count += 1

            res = max(res, count)

            while e < len(end) and s < len(start) and end[e] <= start[s]:
                e += 1
                count -= 1

        return res
    