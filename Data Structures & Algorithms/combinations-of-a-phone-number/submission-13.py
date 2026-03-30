class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = { "2" : "abc",
                        "3" : "def",
                        "4" : "ghi",
                        "5" : "jkl",
                        "6" : "mno",
                        "7" : "pqrs",
                        "8" : "tuv",
                        "9" : "wxyz" }
        
        res = []
        def backtrack(cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for c in digitToChar[digits[len(cur)]]:
                backtrack(cur + c)
            
        if digits: backtrack("")
        return res