class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r: int, c: int, visit: set, prev: int):
            if (r >= ROWS or r < 0 or c >= COLS or c < 0 
            or (r,c) in visit or heights[r][c] < prev
            ):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        # Since we're doing water to water we are going in order of flows if next cell greater than current one
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        ans = []
        
        for (r,c) in pac:
            if (r,c) in atl:
                ans.append([r,c])
        return ans if ans else [[]]