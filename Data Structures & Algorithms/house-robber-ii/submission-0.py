class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp = [0]*n

        dp[1] = nums[1]
        dp[2] = max(nums[1],nums[2])

        for i in range(3, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        curr = dp[-1]

        dp = [0]*n #reset it
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        ans = max(dp[-2], curr)

        return ans