class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        print(dp)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i < len(s) - 1 and (s[i] == "1" or
                    s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
            print(i)
            print(dp)
        return dp[0]