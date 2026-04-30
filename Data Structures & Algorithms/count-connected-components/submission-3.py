class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for adjNode in adjList[node]:
                if adjNode not in visit:
                    dfs(adjNode)

        res = 0
        for node in range(n):
            if node in visit:
                continue
            dfs(node)
            res += 1
        return res