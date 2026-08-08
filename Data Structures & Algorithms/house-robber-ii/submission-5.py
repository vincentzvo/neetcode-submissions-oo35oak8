class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:len(nums) - 1]
        
        one1, two1, one2, two2 = 0, 0, 0, 0
        for i in range(len(nums1)):
            temp1, temp2 = two1, two2
            two1, two2 = max(two1, one1 + nums1[i]), max(two2, one2 + nums2[i])
            one1, one2 = temp1, temp2
        return max(two1, two2)