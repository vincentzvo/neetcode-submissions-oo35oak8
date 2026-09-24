class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()                         # init set

        for t in triplets:                  # traverse each triplet
            if (t[0] > target[0] or             # if any val in cur triplet > corresponding target val:
                t[1] > target[1] or                 # skip triplet
                t[2] > target[2]
            ):
                continue
            
            for i, v in enumerate(t):           # traverse each idx and val of cur triplet:
                if v == target[i]:                  # if cur val = corresponding val in target:
                    res.add(i)                          # add val idx in triplet to set

        return len(res) == 3                # return true if set size = 3 else false