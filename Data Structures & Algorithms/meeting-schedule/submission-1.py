"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)             # sort given intervals list by start values
        
        for i in range(1, len(intervals)):                  # traverse intervals list by idx, skipping first interval:
            if intervals[i - 1].end > intervals[i].start:       # compare end val of prev interval to start val of cur interval:
                return False                                        # return False
        return True                                         # return True if return statement never reached in loop