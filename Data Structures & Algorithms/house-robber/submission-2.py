class Solution:
    def rob(self, nums: List[int]) -> int:
        l = 0
        r = 0

        for i in range(len(nums) - 1, -1, -1):
            temp = max(l, nums[i] + r)
            r = l
            l = temp
        return l