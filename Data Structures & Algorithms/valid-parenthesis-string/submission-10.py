class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0   # init min and max left paren counts

        for c in s:             # traverse each char in string
            if c == "(":            # if cur char left paren
                leftMin += 1            # increm min and max counts
                leftMax += 1
            elif c == ")":          # if cur char right paren
                leftMin -= 1            # decrem min and max counts
                leftMax -= 1
            else:                   # else (cur char star)
                leftMin -= 1            # decrem min count
                leftMax += 1            # increm max count

            if leftMax < 0:         # if max count < 0 (right paren w/out necessary left paren)
                return False            # return false
            if leftMin < 0:         # if min count < 0 (star functioning as left paren)
                leftMin = 0             # reset min count to 0
                
        return leftMin == 0         # return true if min count = 0 else false