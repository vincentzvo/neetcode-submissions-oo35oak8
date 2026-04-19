class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)} # init prereq hashmap with each course mapped to empty list
        for crs, pre in prerequisites:              # for each course prereq pair:
            preMap[crs].append(pre)                     # fill preMap with course as key and prereq as value

        visiting = set()                               # init visit set  

        def dfs(crs):                               # def recursive dfs func with course param
            if crs in visiting:                         # base cases:
                return False                            # if course cur being visited: return false
            if preMap[crs] == []:                       # if course has no prereqs in hash:
                return True                                 # return true

            visiting.add(crs)                           # add cur course to visiting set
            for pre in preMap[crs]:                     # traverse cur course's prereqs in hash
                if not dfs(pre): return False           # run dfs on each prereq and return false if any call returns false
            visiting.remove(crs)                        # remove cur course from visiting set
            preMap[crs] = []                            # set cur course's prereqs to empty in hash
            return True                                 # return true

        for crs in range(numCourses):               # for each course:
            if not dfs(crs): return False               # call dfs on course and return false if call returns false
        return True                                 # return true