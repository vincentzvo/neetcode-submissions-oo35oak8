class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)                 # init res to len nums
        for i in range(len(nums)):      # loop from 0 to n:
            res ^= i ^ nums[i]              # update res to xor itself with i xor nums[i]
        return res                      # return res