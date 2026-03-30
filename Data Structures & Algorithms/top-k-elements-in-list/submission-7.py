class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = {}
        freqArr = [[] for i in range(len(nums) + 1)] # idx = freq/count, val = list of vals

        for n in nums:
            countHash[n] = 1 + countHash.get(n, 0)
        for n, c in countHash.items():
            freqArr[c].append(n)

        res = []
        for i in range(len(freqArr) - 1, 0, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res