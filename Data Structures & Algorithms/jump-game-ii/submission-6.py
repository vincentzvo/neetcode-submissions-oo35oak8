class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0

        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, nums[i] + i)
                l = i + 1
            r = maxJump
            count += 1
        return count