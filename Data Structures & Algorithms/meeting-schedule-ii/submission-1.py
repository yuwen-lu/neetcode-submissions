"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s_intervals = intervals.sort(key=lambda x : x.start)
        queues = []

        for i in intervals:
            flag = False
            for q in queues:
                if self.canSchedule(i, q):
                    q.append(i)
                    flag = True
                    break
            if not flag:
                queues.append([i])
        
        return len(queues)
    
    def canSchedule(self, i: Interval, q: List[Interval]) -> bool:
        for q_i in q:
            if q_i.end > i.start and q_i.end <= i.end:
                return False
            if q_i.start < i.end and q_i.end >= i.end:
                return False
        return True

        