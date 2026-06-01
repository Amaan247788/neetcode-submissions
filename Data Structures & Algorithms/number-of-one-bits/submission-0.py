class Solution:
    def hammingWeight(self, n: int) -> int:
        tally = 0
        for i in range(32):
            tally += n & 1
            n = n >> 1
        return tally