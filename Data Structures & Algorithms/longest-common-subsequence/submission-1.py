class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]    # init dp 2d (t1 len + 1)x(t2 len + 1) list

        for i in range(len(text1) - 1, -1, -1):                     # trav t1 idxs backwards:
            for j in range(len(text2) - 1, -1, -1):                     # trav t2 idxs backwards:
                if text1[i] == text2[j]:                                    # if cur t1 char = cur t2 char:
                    dp[i][j] = 1 + dp[i + 1][j + 1]                             # set dp of idxs to 1 + dp of diagonal DR in dp
                else:                                                       # else (if chars !=):
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])                  # set dp of idxs to max of right cell and left cell

        return dp[0][0]                                             # return top left cell in dp