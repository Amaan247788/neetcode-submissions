from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = defaultdict(int)
        for i in range(len(nums)):
            numToIdx[nums[i]] = i

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in numToIdx:
                if i < numToIdx[rem]:
                    return [i, numToIdx[rem]]
                elif i > numToIdx[rem]:
                    return [numToIdx[rem], i]
        
        return []