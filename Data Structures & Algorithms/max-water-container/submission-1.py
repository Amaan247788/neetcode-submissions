class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l= 0
        r = len(heights) - 1

        while l < r:
            currArea = (r-l) * min(heights[r],heights[l])
            if currArea > maxArea:
                maxArea = currArea
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea
