class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))  # return max of helper call on nums w/out 1st elem, helper call on nums w/out last elem,
                                                                            # and 1st elem (edge case: if nums has exactly 1 elem)
    def helper(self, nums):         # define helper func with nums param for subsets of given nums
        l = 0                           # usual house robber algo
        r = 0
        for n in nums:
            temp = max(r, n + l)            
            l = r
            r = temp
        return r