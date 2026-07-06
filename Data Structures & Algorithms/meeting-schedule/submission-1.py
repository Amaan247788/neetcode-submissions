"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        #brute force - sort and check for overlap
        intervals.sort(key = lambda i: i.start)
        prevE = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prevE:
                return False
            prevE = interval.end
        return True