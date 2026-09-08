class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]                    # init maxSubArray var to 1st elem in nums
        curSum = 0                          # init curSum var to 0

        for n in nums:                      # traverse each num in nums:
            if curSum < 0:                      # if curSum after prev loop is negative:
                curSum = 0                          # reset curSum to 0
            curSum += n                         # add cur num to curSum
            maxSub = max(maxSub, curSum)        # update maxSub to max of cur vals and curSum

        return maxSub                       # return maxSub