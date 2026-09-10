class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0                                       # init count to 0
        l = r = 0                                       # init left and right ptrs to 0

        while r < len(nums) - 1:                        # loop until right ptr reaches last index of nums:
            farthest = 0                                    # (re)set farthest to 0
            for i in range(l, r + 1):                       # traverse by idx nums from left to right ptr:
                farthest = max(farthest, nums[i] + i)           # update farthest to max of itself and cur num + cur idx
            l = r + 1                                       # shift left ptr to 1 past right ptr
            r = farthest                                    # shift right ptr to farthest
            count += 1                                      # increm count
        return count                                    # return count