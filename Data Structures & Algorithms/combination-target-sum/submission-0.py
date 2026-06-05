class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [],[]
        # nums.sort()

        def backtrack(i):
            tally = sum(sol)
            if i == n:
                return
            if tally == target:
                res.append(sol[:])
                return
            
            #Taking the same number again
            if tally + nums[i] <= target:
                sol.append(nums[i])
                backtrack(i)
                sol.pop()
            
            #Taking the next number
            backtrack(i+1)
        
        backtrack(0)
        return res
            
            