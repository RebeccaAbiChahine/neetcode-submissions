class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = {}
        for i in range(numCourses):
            prerequisiteMap[i] = []
        
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)

        visit = set()

        def dfs(course):
            if course in visit:
                return False

            if prerequisiteMap[course] == []:
                return True
            
            visit.add(course)

            for prerequisite in prerequisiteMap[course]:
                if not dfs(prerequisite):
                    return False

            visit.remove(course)
            prerequisiteMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course): 
                return False

        return True
