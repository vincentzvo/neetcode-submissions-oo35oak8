class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            #print(maxHeap)
            #print(q)
            time += 1
            #if time > 20: break
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    q.append([cnt + 1, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time