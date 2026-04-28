class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        cycle = set()

        def dfs(node, prev):
            if node in cycle:
                return False
            
            cycle.add(node)
            for adj in adjList[node]:
                if adj == prev:
                    continue
                if not dfs(adj, node):
                    return False
            #cycle.remove(node)
            return True

        res = dfs(0, -1)
        print(cycle)
        return res if len(cycle) == n else False