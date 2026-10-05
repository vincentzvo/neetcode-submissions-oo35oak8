class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }                 # init adj list with every char as key to empty set

        for i in range(len(words) - 1):                             # traverse words by idx (exempt last):
            w1, w2 = words[i], words[i + 1]                             # store word at cur and next idx
            minLen = min(len(w1), len(w2))                              # calc and store min len b/w words
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:        # if latter word is prefix of former word:
                return ""                                                   # return empty str b/c given ordering invalid
            for j in range(minLen):                                     # traverse chars in words:
                if w1[j] != w2[j]:                                          # if chars of words at cur idx don't match:
                    adj[w1[j]].add(w2[j])                                       # add latter word's char to former word's char in adj list
                    break                                                       # break

        visit = {}                  # init visit hash map
        res = []                    # init res list

        def dfs(c):                 # def recurs dfs func w/ char/node param:
            if c in visit:              # if char in visit:
                return visit[c]             # return val to char key in visit. True if in cur path, false if visited
            
            visit[c] = True             # set char's val in visit to true
            
            for nei in adj[c]:          # traverse char's neighbors in adj list:
                if dfs(nei):                # if recurse call on neighbor returns true:
                    return True                 # return true
            
            visit[c] = False            # set char's val in visit to false
            res.append(c)               # add char to res list

        for c in adj:               # traverse chars in adj list:
            if dfs(c):                  # if recurse call on neighbor returns true:
                return ""                   # return ""
        res.reverse()               # reverse res list in place
        return "".join(res)         # return joined res list