class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set(nums)
        return len(dups) != len(nums)