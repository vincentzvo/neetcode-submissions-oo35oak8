class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            if n in hashset:
                hashset.discard(n)
            else:
                hashset.add(n)
        return list(hashset)[0]