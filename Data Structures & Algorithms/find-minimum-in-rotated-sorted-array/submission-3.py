class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while nums[l] > nums[r]:
            r = r - 1
        
        return nums[r + 1]