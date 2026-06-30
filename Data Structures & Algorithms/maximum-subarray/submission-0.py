class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #remove the negative prefix
        curr = 0
        maxSum = nums[0]

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxSum = curr if curr > maxSum else maxSum
        return maxSum


        