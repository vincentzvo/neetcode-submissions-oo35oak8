class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                if nums[l] < nums[r]:
                    res = min(res, nums[l])
                    r = m - 1
                else:
                    res = min(res,nums[m])
                    l = m + 1
            else:
                if nums[m] < nums[r]:
                    res = min(res,nums[m])
                    r = m - 1
                else:
                    res = min(res,nums[m])
                    l = m + 1

        return res