class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()

        def dfs(node, prev, adjList):
            if node in visit:
                return False
            
            visit.add(node)
            for adjNode in adjList[node]:
                if adjNode == prev:
                    continue
                if not dfs(adjNode, node, adjList):
                    return False
            return True
            
        for i in range(len(edges) - 1, -1, -1):
            curGraph = edges[:i] + edges[i + 1:]
            adjList = defaultdict(list)
            for n1, n2 in curGraph:
                adjList[n1].append(n2)
                adjList[n2].append(n1)
            
            flag = True
            for j in range(1, len(adjList)):
                if j not in visit:
                    if not dfs(j, 0, adjList):
                        flag = False
                        break
            if flag:
                return edges[i]
            visit.clear()
        return []