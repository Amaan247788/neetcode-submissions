"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        print(starts)
        print(ends)
        ends.sort()
        
        count = 0
        maxCount = 0

        s = 0
        e = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            maxCount = max(maxCount, count)
        return maxCount