class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses) }    # init hashmap with key: crs, val: list of prereqs
        for crs, pre in prerequisites:                  # fill hashmap
            preMap[crs].append(pre)

        visit = set()                                   # init set to store already visited courses
        cycle = set()                                   # init set to store courses in current path
        res = []                                        # init res list

        def dfs(crs):                                   # define recursive dfs func with course param:
            if crs in cycle:                                # Base Cases:
                return False                                    # if course in cycle return false
            if crs in visit:                                    # if course in visit return true
                return True
            
            cycle.add(crs)                                  # add course to cycle
            for pre in preMap[crs]:                         # for each of the course's prereqs:
                if not dfs(pre): return False                   # call dfs on the prereq and return false if the call returns false
            cycle.remove(crs)                               # remove course from cycle if no prereqs return false
            visit.add(crs)                                  # add course to visit
            res.append(crs)                                 # append course to res list
            return True                                     # return true

        for crs in range(numCourses):                   # for every course:
            if not dfs(crs): return []                      # call dfs on course and return empty list if any return false

        return res                                      # return res list if no course returns false