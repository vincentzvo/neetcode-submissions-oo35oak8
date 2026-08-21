class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)                        # init array w/ 1 for each num

        for i in range(len(nums) - 1, -1, -1):      # traverse nums backwards by idx:
            for j in range(i + 1, len(nums)):           # traverse nums between cur i num and end of nums:
                if nums[i] < nums[j]:                       # if cur i num is less than cur j num:
                    dp[i] = max(dp[i], dp[j] + 1)               # update array at cur i to max of cur val and val at cur j + 1
        
        return max(dp)                              # return max val in dp