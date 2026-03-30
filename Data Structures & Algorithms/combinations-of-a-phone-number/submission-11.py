class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashset = {"2" : "abc",                 # maps digits to characters
                   "3" : "def",
                   "4" : "ghi",
                   "5" : "jkl",
                   "6" : "mno",
                   "7" : "pqrs",
                   "8" : "tuv",
                   "9" : "wxyz"}
        
        res = []                             # init res
        def backtrack(cur):                  # recurs backtrack func w/ curStr
            if len(cur) == len(digits):             # base case: if curStr len = digs len
                res.append(cur)                         # add curStr to res 
                return                                  # end this path
            
            for c in hashset[digits[len(cur)]]:            # for each char corresponding to cur digit
                backtrack(cur + c)               # recurs w/ next dig and new curStr
        
        if digits: backtrack("")             # if digs not empty: run algo
        return res                              # return res
