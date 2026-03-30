class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("A") and ord(c) <= ord("Z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")):
                ss += c.lower()
        
        front = 0
        back = len(ss) - 1

        while front < back:
            if (ss[front] == ss[back]):
                front += 1
                back -= 1
            else:
                return False
        return True