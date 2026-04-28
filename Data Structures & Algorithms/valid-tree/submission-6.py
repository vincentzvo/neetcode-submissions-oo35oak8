class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for adj in adjList[node]:
                if adj == prev:
                    continue
                if not dfs(adj, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n