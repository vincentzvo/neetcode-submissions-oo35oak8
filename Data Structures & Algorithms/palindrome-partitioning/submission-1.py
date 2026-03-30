class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []                                    # init res and partition lists
        part = []

        def dfs(i):                                 # recurs func
            if i >= len(s):                             # base case: if i gets to end of str
                res.append(part.copy())                     # append copy of part to res and return
                return
            
            for j in range(i, len(s)):              # loop j from i to end of str
                if self.isPalindrome(s, i, j):          # helper function call: if substring from i to j is palindrome:
                    part.append(s[i:j + 1])                 # append substring to part
                    dfs(j + 1)                              # call recurs on remaining string
                    part.pop()                              # pop fron partition
        
        dfs(0)                                      # call dfs on 0
        return res                                  # return res
    
    def isPalindrome(self, s, l, r):            # helper function
        while l < r:                                # while l ptr < r ptr
            if s[l] != s[r]:                            # is l str != r str: return False
                return False
            l += 1                                      # increm l prt
            r -= 1                                      # decrem r ptr
        return True                                 # return True
        