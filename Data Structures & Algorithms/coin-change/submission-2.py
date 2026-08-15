class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)    # init dp array w/ default val amnt+1 for idx 0-amnt
        dp[0] = 0                           # set 0 idx to 0 for edge case

        for a in range(1, amount + 1):  # traverse each amount exept for 0
            for c in coins:               # traverse each coin
                if a - c >= 0:              # if cur coin can be subtracted from cur amnt w/out going neg
                    dp[a] = min(dp[a], 1 + dp[a - c])   # set dp for cur amnt to min of cur val and 1 + dp
                                                        # of cur amnt - cur coin
        return dp[amount] if dp[amount] != amount + 1 else -1   # return dp amnt unless default val never
                                                                # overwritten, then return -1