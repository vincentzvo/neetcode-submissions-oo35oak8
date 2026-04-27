class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if preMap[crs] == []:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True