from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # so no child can have two parents
        if not n:
            return True
        
        visited = set()
        neighbors = defaultdict(list, {i: [] for i in range(n)})

        for par,child in edges:
            neighbors[par].append(child)
            neighbors[child].append(par)

        def dfs(i: int, prev: int) -> bool:
            # if node has no neighbors
            if i in visited:
                return False
            # if all its neighbors visited or prev
            visited.add(i)
            for neighbor in neighbors[i]:
                if neighbor != prev:
                    if not dfs(neighbor, i):
                        return False
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n
            

