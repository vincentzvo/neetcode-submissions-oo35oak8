class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)                 # init adjList hashmap
        for src, dst in sorted(tickets)[::-1]:  # traverse sorted tickets list backwards
            adj[src].append(dst)                    # add dest airport to src airports list in adjList
        
        res = []                                # init empty res list
        def dfs(src):                           # def recursive dfs func with src airport param
            while adj[src]:                         # while cur src airport has dst airports in adjList
                dst = adj[src].pop()                    # pop and store from cur airports adjList
                dfs(dst)                                # call dfs recursively on dst airport
            res.append(src)                         # once all src's dst airports called, add src airport to res

        dfs("JFK")                              # call dfs on starting airport
        return res[::-1]                        # return res list reversed