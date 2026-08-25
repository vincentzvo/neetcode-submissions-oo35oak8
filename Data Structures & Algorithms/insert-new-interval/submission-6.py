class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        flag = True

        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                if flag:
                    res.append(newInterval)
                    flag = False
                res.append(i)
            else:
                newInterval = ([min(i[0], newInterval[0]),max(i[1], newInterval[1])])
                flag = True
        if flag:
            res.append(newInterval)
        return res