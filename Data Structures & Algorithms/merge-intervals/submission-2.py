class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = ans[-1][1]
            if start <= lastEnd:
                #Overlap exists
                ans[-1] = [min(ans[-1][0], start), max(ans[-1][1], end)]
            else:
                ans.append([start, end])
        return ans