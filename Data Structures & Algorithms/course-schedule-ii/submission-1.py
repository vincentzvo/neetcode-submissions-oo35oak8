class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for pre in range(numCourses):
            if not dfs(pre): return []

        return list(res)