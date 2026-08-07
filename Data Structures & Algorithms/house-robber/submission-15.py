class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        one, two = nums[0], nums[1]
        for i in range(2, len(nums)):
            temp = two
            two = nums[i] + one
            one = max(temp, one)
        return max(one, two)