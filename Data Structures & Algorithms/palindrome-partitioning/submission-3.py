class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []                              # init res and partition arrays

        def dfs(i):
            if i >= len(s):                             # base case: i gets to end of string
                res.append(part.copy())                 # add copy of part to res
            
            for j in range(i, len(s)):                  # for loop for substrings
                if self.isPalindrome(s[i:j + 1]):           # if substr is palindrome:
                    part.append(s[i:j + 1])                     # add substr to part list
                    dfs(j + 1)                                  # recurse starting at rest of str
                    part.pop()                                  # remove part 
        dfs(0)
        return res
    
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
