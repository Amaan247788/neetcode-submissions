import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def numOnes(number: int) -> int:
            tally = 0
            bits = math.log2(number)
            for i in range(int(bits)+1):
                lsb = number & 1
                tally += lsb
                number = number >> 1
            return tally
        
        ans = [0]
        for i in range(1, n+1):
            ans.append(numOnes(i))
        return ans