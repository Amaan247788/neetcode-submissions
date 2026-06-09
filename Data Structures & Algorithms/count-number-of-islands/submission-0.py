class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markIsland(x:int, y:int) -> None:
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
                return
            
            grid[x][y] = "X"
            
            markIsland(x+1, y)
            markIsland(x, y-1)
            markIsland(x-1, y)
            markIsland(x, y+1)

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIslands += 1
                    markIsland(i,j)
        
        return numIslands