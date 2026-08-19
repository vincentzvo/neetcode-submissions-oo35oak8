class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)                             # init res to max in nums
        curMin, curMax = 1, 1                       # init cur min & max both to 1

        for n in nums:                              # traverse each num in given list:
            temp = curMax * n                           # store cur max * cur num in temp var
            curMax = max(n * curMax, n * curMin, n)     # update cur max to max of n*max, n*min, and n
            curMin = min(temp, n * curMin, n)           # update cur min to max of old n*max, n*min, and n
            res = max(res, curMax)                      # update res to max of itself and curmax
            
        return res                                  # return res