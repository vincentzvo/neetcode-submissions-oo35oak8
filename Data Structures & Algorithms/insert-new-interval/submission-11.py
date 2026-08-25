class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []                                                    # init list to be returned

        for i in range(len(intervals)):                             # traverse list of ints by index
            if newInterval[1] < intervals[i][0]:                        # if newInt doesn't overlap and is lesser than cur:
                res.append(newInterval)                                     # append newInt to res list
                return res + intervals[i:]                                  # return res list + rest of intervals list
            elif newInterval[0] > intervals[i][1]:                      # elif newInt doesn't overlap and is greater than cur:
                res.append(intervals[i])                                    # append cur int to res
            else:                                                       # else (if newInt and cur overlap):
                newInterval = [min(newInterval[0], intervals[i][0]),        # update newInt to have min and max values of
                               max(newInterval[1], intervals[i][1])]        # newInt and cur int

        res.append(newInterval)                                     # append newInt to res
        return res                                                  # return res