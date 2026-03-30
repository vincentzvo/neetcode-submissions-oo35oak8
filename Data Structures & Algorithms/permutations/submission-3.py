class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:                  # base case
            return [[]]
        
        perms = self.permute(nums[1:])      # recursively return nums w/ out first element until len 0
        res = []                            # init res

        for p in perms:                     # trav all incomplete perms in perms
            for i in range(len(p) + 1):     # trav all possible locs to insert nums[0] into each perm
                p_copy = p.copy()           # create copy of cur perm
                p_copy.insert(i, nums[0])   # insert nums[0] at i in cur perm copy
                res.append(p_copy)          # append cur perm copy into res for recursion or final output
        
        return res                          # return res upt to previous recursive call or output