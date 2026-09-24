class Solution:
    def checkValidString(self, s: str) -> bool:
        lpStack = []
        starStack = []

        for i, c in enumerate(s):
            if c == "(":
                lpStack.append(i)
            elif c == "*":
                starStack.append(i)
            elif lpStack:
                lpStack.pop()
            elif starStack:
                starStack.pop()
            else:
                return False

        while lpStack and starStack:
            lpCur = lpStack.pop()
            starCur = starStack.pop()

            if lpCur > starCur:
                return False
        
        return not lpStack