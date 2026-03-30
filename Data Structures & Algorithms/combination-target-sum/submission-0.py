class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return res
            elif sum(subset) > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        print(res)
        return res