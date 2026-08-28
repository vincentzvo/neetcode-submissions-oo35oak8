class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()                                    # sort intervals list
        minHeap = []                                        # init minheap list
        res = {}                                            # init res hash
        i = 0                                               # init ptr for intervals list

        for q in sorted(queries):                           # traverse every query in sorted queries list:
            while i < len(intervals) and intervals[i][0] <= q:  # while ptr in bounds and cur intervals start is before query val:
                start, end = intervals[i]                           # set/update start and end vars to cur intervals
                heapq.heappush(minHeap, (end - start + 1, end))     # push pair w/ cur interval len and end to minheap
                i += 1                                              # increm ptr
            
            while minHeap and minHeap[0][1] < q:                # while minheap isnt empty and the top interval's end is < cur query:
                heapq.heappop(minHeap)                              # pop from minHeap

            res[q] = minHeap[0][0] if minHeap else -1           # add to res hash cur query : top intervals len if minheap isnt empty else -1

        return [res[q] for q in queries]                    # return built list of val in res hash for each query in queries