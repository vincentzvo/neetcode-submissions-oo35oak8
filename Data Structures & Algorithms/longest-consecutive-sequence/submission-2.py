class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums2 = list(set(nums))
        nums2.sort()
        print(nums2)
        res = 1
        cur = 1
        for i in range(1, len(nums2)):
            if nums2[i] - 1 == nums2[i - 1]:
                cur += 1
            else:
                if cur > res:
                    res = cur
                cur = 1
            if (i == len(nums2) - 1):
                if cur > res:
                    res = cur
        return res