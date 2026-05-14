class Solution:
    def rob(self, nums: List[int]) -> int:
        l = 0
        r = 0
        
        for i in range(len(nums)):
            temp = r
            r = max(r, nums[i] + l)
            l = temp
        return r
