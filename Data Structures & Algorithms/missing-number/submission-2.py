class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_indices = 0
        sum_nums = 0
        
        for i, num in enumerate(nums):
            sum_indices += i
            sum_nums += num
        
        sum_indices += len(nums)
        
        total = sum_indices - sum_nums
        
        return total