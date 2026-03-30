class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1 if len(s) > 0 else 0
        for i in range(len(s) - 1):
            subStr = "" + s[i]
            j = i + 1
            while j < len(s) and s[j] not in subStr:
                subStr += s[j]
                print(subStr)
                j += 1
            res = max(res, len(subStr))
        return res