from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need to make a minheap and while size is greater than k just pop
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        minheap = []
        
        for key,val in freq.items():
            heapq.heappush(minheap, (val, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        ans = []
        while len(minheap) > 0:
            val, key = heapq.heappop(minheap)
            ans.append(key)
        return ans