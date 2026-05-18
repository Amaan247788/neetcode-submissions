class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search given away by asking for O(log n)
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[0]