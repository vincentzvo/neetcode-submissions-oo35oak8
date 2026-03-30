class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #print(stack[-1][0])
                stackT, stackIdx = stack[-1]
                print(stackT)
                print(stackIdx)
                res[stackIdx] = i - stackIdx
                stack.pop()
            print([t,i])
            stack.append([t,i])

        return res