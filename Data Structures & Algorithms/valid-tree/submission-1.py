class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True                           # edge case: if no nodes then technically valid
        
        adj = { i:[] for i in range(n) }                # init adjacency hash map node:node
        for n1, n2 in edges:                            # for each pair of nodes:
            adj[n1].append(n2)                              # append to eachothers list
            adj[n2].append(n1)
        visit = set()                                   # init visit set

        def dfs(node, prev):                            # define recursive dfs func with node and prevNode params
            if node in visit:                               # base case:
                return False                                # if node in visit set (cycle): return false
            
            visit.add(node)                                 # add node to visit set
            for i in adj[node]:                             # for every node adj to cur node:
                if i == prev:                                   # if adj node is prev node: continue
                    continue
                if not dfs(i, node): return False               # if dfs call on adj node with cur node as prev returns false: return false
            return True                                     # return true if no call on adj nodes returns false

        return dfs(0, -1) and len(visit) == n           # return dfs call on 0 node with dummy prev and check that every node was visited