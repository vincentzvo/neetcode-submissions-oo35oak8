class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}                        # init hashmap
        for i, c in enumerate(s):           # traverser idx and chars in enumerated s str
            lastIdx[c] = i                      # map chars in s to last idx    
        
        res = []                            # init res list
        size = end = 0                      # init size and end vars to 0
        for i, c in enumerate(s):           # traverser idx and chars in enumerated s str
            size += 1                           # increm size
            end = max(end, lastIdx[c])          # update end to max of end and lastIdx of cur char

            if i == end:                        # if cur idx = max last idx of chars in cur partition
                res.append(size)                    # add size to res list
                size = 0                            # reset size to 0 for next partition
        return res                          # return res
