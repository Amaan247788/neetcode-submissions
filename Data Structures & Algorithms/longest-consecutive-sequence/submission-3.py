class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        contains = set()
        for num in nums:
            contains.add(num)

        longest = 1

        for num in contains:
            curr = 1
            if (num-1) in contains:
                continue
            else:
                start = num
                while start+1 in contains:
                    start += 1
                    curr += 1
                    longest = max(curr, longest)
        
        return longest
