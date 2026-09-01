class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prevEnd = res[-1][1]

            if start > prevEnd:
                res.append([start, end])
            else:
                res[-1][1] = max(end, prevEnd)

        return res