class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for n in nums:
            if n in hashset:
                return True
            hashset[n] = 1
        return False