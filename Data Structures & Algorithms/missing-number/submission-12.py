class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

        # [1,2,3]
            # res = 3       |   011
            # res ^= 0 ^ 1  |   011 ^ 000 ^ 001 = 010
            # res ^= 1 ^ 2  |   010 ^ 001 ^ 010 = 001
            # res ^= 2 ^ 3  |   001 ^ 010 ^ 011 = 000
        # [0,2]
            # res = 2       |
            # res ^= 0 ^ 0  |
            # res ^= 1 ^ 2  |
        # [0,1,2]
            # res = 3       |
            # res ^= 0 ^ 0  |
            # res ^= 1 ^ 1  |
            # res ^= 2 ^ 2  |