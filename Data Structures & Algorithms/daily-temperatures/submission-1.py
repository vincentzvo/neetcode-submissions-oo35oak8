class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
                
                if j == len(temperatures) - 1:
                    res.append(0)
        
        return res