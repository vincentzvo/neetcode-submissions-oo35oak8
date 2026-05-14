class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        
        for i in range(2, len(nums)):
            print(nums[i - 2])
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        print(nums)
        return max(nums[len(nums) - 1], nums[len(nums) - 2])

    """

    [5,1,2,10,6,2,7,9,3,1]
    i:            2- 3-4-5-6-7-8-9
    nums[i]-: 5-1-2-10- 6- 2- 7- 9- 3- 1
    nums[i]+: 5-1-7-11-13-13-20-22-23-23

    """