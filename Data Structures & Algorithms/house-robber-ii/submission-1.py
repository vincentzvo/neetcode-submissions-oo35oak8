class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:len(nums) - 1]
        l1 = 0
        r1 = 0
        l2 = 0
        r2 = 0

        for i in range(len(nums) - 1):
            temp1 = max(r1, nums1[i] + l1)
            l1 = r1
            r1 = temp1

            temp2 = max(r2, nums2[i] + l2)
            l2 = r2
            r2 = temp2
        return max(r1, r2) if len(nums) > 1 else nums[0]
