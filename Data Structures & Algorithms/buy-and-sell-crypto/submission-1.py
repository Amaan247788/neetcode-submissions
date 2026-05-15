class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i think this is two pointer again
        # let i be your
        best = 0
        l = 0
        r = l + 1
        while r < len(prices):
            curr = prices[r] - prices[l]
            best = max(best, curr)
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return best