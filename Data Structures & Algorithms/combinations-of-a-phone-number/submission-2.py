class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashset = {'2' : ['a', 'b', 'c'],
                   '3' : ['d', 'e', 'f'],
                   '4' : ['g', 'h', 'i'],
                   '5' : ['j', 'k', 'l'],
                   '6' : ['m', 'n', 'o'],
                   '7' : ['p', 'q', 'r', 's'],
                   '8' : ['t', 'u', 'v'],
                   '9' : ['w', 'x', 'y', 'z']}
        
        res = []
        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            
            for c in hashset[digits[i]]:
                dfs(i + 1, cur + c)
        
        dfs(0, "")
        return res if digits else []
