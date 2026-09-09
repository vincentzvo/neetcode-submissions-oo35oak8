class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1                        # init goal to last idx of nums list

        for i in range(len(nums) - 2, -1, -1):      # traverse nums backwards by idx starting at penultimate idx
            if i + nums[i] >= goal:                     # if cur idx can reach goal idx:
                goal = i                                    # update goal to cur idx
        
        return goal == 0                            # return goal = 0 so true if reached idx 0 else false