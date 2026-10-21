class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0             # init res to 0
        for n in nums:      # traverse each num in nums:
            res ^= n            # update res to res xor cur num
        return res          # return res