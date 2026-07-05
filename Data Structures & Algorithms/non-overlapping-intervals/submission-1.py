class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: (i[1], i[0]))
        combinable = 0

        prevE = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevE:
                combinable += 1
                # want the smaller end so leave as is
            else:
                # since ends are sorted and theres no overlap go to next end
                prevE = intervals[i][1]
        return combinable
