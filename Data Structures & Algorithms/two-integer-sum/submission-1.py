from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[nums[i]] = i