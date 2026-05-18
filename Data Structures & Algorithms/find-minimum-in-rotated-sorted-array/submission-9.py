class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search given away by asking for O(log n)
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]