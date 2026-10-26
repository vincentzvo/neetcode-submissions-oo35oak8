class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        for i in range(len(nums)):
            if i not in hashset:
                return i
        return len(nums)