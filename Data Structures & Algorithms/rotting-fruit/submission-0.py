class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #0 - empty, 1 - fresh fruit, 2 - rotten fruit
        q = deque()
        time, fresh = 0, 0
        '''
        First we need to find the rotten fruit then do a dfs to see how
        we can connect all the fresh fruit and time it by iteration
        '''
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                num = grid[row][col]
                if num == 1:
                    fresh += 1
                elif num == 2:
                    q.append([row,col])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:

            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    #make sure its in bounds and not rotten, make it rotten
                    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
