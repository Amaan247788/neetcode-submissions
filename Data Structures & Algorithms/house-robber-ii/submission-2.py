class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        def helper(nums):
            rob1, rob2 = 0,0

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        ans = max(helper(nums[1:]), helper(nums[:-1]))
        return ans