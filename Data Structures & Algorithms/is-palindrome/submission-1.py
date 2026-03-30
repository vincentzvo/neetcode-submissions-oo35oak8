class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("A") and ord(c) <= ord("Z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")):
                ss += c.lower()

        bwss = ""
        for i in range(len(ss) - 1, -1, -1):
            bwss += ss[i]
        
        return ss == bwss