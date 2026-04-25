class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First, we need to initialize a hash map to map the course to prereqs
        preMap = {i:[] for i in range(numCourses)} # 0:[], 1:[], 2:[], 3:[], 4:[] with numCourses = 5

        for crs, pre in prerequisites: # prerequisites are edges
            preMap[crs].append(pre) # crs:[pre] EX: 0:[1]

        visitSet = set() # all courses alone the curr DFS path
        def dfs(crs):
            if crs in visitSet:
                return False # Impossible to finish all courses cuz we have detected a loop
            if preMap[crs] == []: # crs has no prereqs, it's possible to finish, we return True
                return True 
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs) # we are no longer running dfs on this crs
            preMap[crs] = [] # set it to empty list so we could immediately return True when revisited
            return True
        
        # 1 -> 2
        # 3 -> 4
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
