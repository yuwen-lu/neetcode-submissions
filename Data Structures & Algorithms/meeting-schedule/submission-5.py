"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_intervals = sorted(intervals, key=lambda x:x.start)

        for idx, i in enumerate(s_intervals):

            if idx + 1 == len(s_intervals):
                return True

            start = i.start
            end = i.end
            next_start = s_intervals[idx+1].start
            next_end = s_intervals[idx+1].end

            if end > next_start:
                return False

        return True