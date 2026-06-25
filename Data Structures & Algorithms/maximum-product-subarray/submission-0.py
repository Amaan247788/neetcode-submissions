class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)
        currMin, currMax = 1,1

        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            tmp = currMax * n
            currMax = max(currMax*n, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            best = max(best, currMax)
        return best
        

