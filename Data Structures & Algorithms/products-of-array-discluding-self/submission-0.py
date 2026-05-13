class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Make an array of left product
        left = [1]
        left_prod = 1
        for i in range(0,len(nums)):
            left_prod *= nums[i]
            left.append(left_prod)
        # Make an array of right products
        right = [1]*len(nums)
        right_prod = 1
        for i in range(len(nums)-1, 0, -1):
            right_prod *= nums[i]
            right[i-1] = right_prod
        # Make final array with products of left times right to get product excluding self
        final = []
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        
        return final