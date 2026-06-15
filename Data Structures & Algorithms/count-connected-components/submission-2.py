from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list[int])

        for i in range(n):
            graph[i] = []
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #adjacency list built

        visited = set()

        def dfs(i: int):
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
                