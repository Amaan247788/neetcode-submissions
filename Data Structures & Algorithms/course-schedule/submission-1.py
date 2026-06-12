from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make a directed graph - if cyclic return false
        # there are 0 to numCourses - 1 courses
        graph = defaultdict(list[int])
        for i in range(numCourses):
            graph[i] = []
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visiting = set()

        def dfs(curr):
            if curr in visiting:
                return False
            
            if graph[curr] == []:
                return True

            visiting.add(curr)
            for prereq in graph[curr]:
                if not dfs(prereq):
                    return False
            visiting.remove(curr)
            graph[curr] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        