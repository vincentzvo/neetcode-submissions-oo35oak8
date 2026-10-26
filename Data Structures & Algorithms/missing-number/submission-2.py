class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != sorted(nums)[i]:
                return i
        return len(nums)