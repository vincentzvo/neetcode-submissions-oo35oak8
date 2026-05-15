class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        l = 0
        r = 0
        for n in nums:
            temp = max(r, n + l)
            l = r
            r = temp
        return r