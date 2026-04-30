class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]         # init parent list with each node
        rank = [1] * n                      # init rank list with 1 for each node

        def find(node):                     # func to find nodes greatest parent with node param:
            res = node                          # init res to input node

            while res != par[res]:              # while res node is not its own parent:
                par[res] = par[par[res]]            # set res node parent to res nodes grand parent
                res = par[res]                      # set res node to its parent
            return res                          # return res node

        def union(n1, n2):                  # func to union 2 nodes wit h2 node params:
            p1, p2 = find(n1), find(n2)         # init parent 1 and parent 2 to find calls on each node

            if p1 == p2:                        # if nodes have the same parent:
                return 0                            # return 0

            if rank[p2] > rank[p1]:             # if parent 2s tree is larger:
                par[p1] = p2                        # set parent 1s parent as parent 2
                rank[p2] += rank[p1]                # add parent 1s rank to parent 2s rank
            else:                               # else (p1s tree larger):
                par[p2] = p1                        # set p2s parent as p1
                rank[p1] += rank[p2]                # add p2s rajk to p1s rank
            return 1                            # return 1

        res = n                             # init res as number of nodes
        for n1, n2 in edges:                # for every pair of nodes sharing an edge:
            res -= union(n1, n2)                # dectrment res by 1 for each new union
        return res                          # return res
