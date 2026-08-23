class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:                           # if sum of nums is odd:
            return False                                # return False (impossible)
            
        dp = set()                                  # init dp set
        dp.add(0)                                   # add init val of 0 to dp
        target = sum(nums) // 2                     # init target var to half of sum of nums

        for i in range(len(nums) - 1, -1, -1):      # traverse nums list backwards:
            nextDp = set()                              # init/reset nextDp to new set
            for n in dp:                                # traverse all nums in cur dp:
                if nums[i] + n == target:                   # if cur num in list + cur num in dp = target:
                    return True                                 # return True
                nextDp.add(n)                               # add cur num in dp to nextDp
                nextDp.add(nums[i] + n)                     # add cur num in dp + cur num in list to nextDp
            dp = nextDp                                 # update dp to nextDp
        return False                                # return False (reached if for loop exits w/out reaching True return)