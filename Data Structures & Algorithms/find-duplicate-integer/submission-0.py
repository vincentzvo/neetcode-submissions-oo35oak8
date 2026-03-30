class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cur = nums[i]
            del nums[i]
            if cur in nums:
                return cur
            nums.append(cur)