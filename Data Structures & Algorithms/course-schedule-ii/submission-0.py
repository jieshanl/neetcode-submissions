class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Graph Traversal
        # build an adjacency List of prereqs
        # Topological Sort
        # use a set to detect any cycles

        prereq = { c:[] for c in range(numCourses)}

        # iterate through every course-prereq pair in prerequisites list
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        # Time Complexity: O(V + E)
        # Space Complexity: O(V + E)
        # V is the number of courses and E is the number of prereqs


