class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:
            temp = curMin
            curMin = min(curMin * n, curMax * n, n)
            curMax = max(temp * n, curMax * n, n)
            res = max(res, curMax)
        
        return res