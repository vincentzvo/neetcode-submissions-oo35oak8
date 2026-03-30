class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        arr = [0] * k
        for i in range(k):
            max = 0
            for c in hashmap:
                if hashmap[c] > hashmap.get(max, 0):
                    max = c
            arr[i] = max
            del hashmap[max]
        return arr