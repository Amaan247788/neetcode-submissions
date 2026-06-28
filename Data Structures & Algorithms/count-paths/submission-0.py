class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m rows, n cols
        #only allowed to go right or down
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
