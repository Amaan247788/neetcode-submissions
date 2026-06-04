class Solution:
    def reverseBits(self, n: int) -> int:
        final = 0
        for i in range(32):
            lsb = n & 1
            final |= (lsb << (32- i - 1))
            n = n >> 1
        return final