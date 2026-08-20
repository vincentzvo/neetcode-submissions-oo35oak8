class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)             # init array with false for each char in s + 1 for start
        dp[-1] = True                           # set starting position at end of dp array to true

        for i in range(len(s) - 1, -1, -1):     # traverse str backwards by index:
            for word in wordDict:                   # for each word in wordDict:
                if word == s[i:i + len(word)]:          # if the word matches the substr from cur idx w/ same len:
                    dp[i] = dp[i + len(word)]               # update dp[i] to val in dp as far back as the len of the word
                    if dp[i]:                               # if dp at idx i's val is true:
                        break                                   # break (so isn't overridden)

        return dp[0]                            # return first val in dp that represents entire str