class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i think this is two pointer again
        # let i be your
        best = 0
        for i in range(len(prices)):
            r = len(prices) - 1
            while i < r:
                curr = prices[r] - prices[i]
                best = max(curr, best)
                r -= 1
        
        return best