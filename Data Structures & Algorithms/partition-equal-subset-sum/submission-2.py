class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, curSum):
            if curSum == sum(nums) / 2:
                return True
            if i == len(nums):
                return False

            return dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum)
        
        return dfs(0, 0)