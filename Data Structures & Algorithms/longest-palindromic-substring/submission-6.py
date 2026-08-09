class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""       # global res vars
        self.resLen = 0

        def helper(l, r):                                   # nested helper
            while l >= 0 and r < len(s) and s[l] == s[r]:       # while palindrome and not at edge
                if r - l + 1 > self.resLen:                         # if new longest
                    self.res = s[l:r+1]                                 # update res vars
                    self.resLen = r - l + 1
                l -= 1                                              # shift ptrs
                r += 1

        for i in range(len(s)):
            helper(i, i)        # odd len
            helper(i, i + 1)    # even len

        return self.res         # return res