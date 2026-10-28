class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)                  # init dp list with 0s from 0-n
        offset = 1                          # init offset var to 1

        for i in range(1, n + 1):           # loop from 1 to n:
            if offset * 2 == i:                 # if i is = to offset * 2:
                offset = i                          # update offset to i
            dp[i] = 1 + dp[i - offset]          # set dp at cur idx to 1 + dp at i - offset 

        return dp                           # return dp