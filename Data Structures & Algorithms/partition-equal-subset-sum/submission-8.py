class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDp.add(t)
                nextDp.add(t + nums[i])
            dp = nextDp
        return False