"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = []
        for i,interval in enumerate(intervals):
            l.append([interval.start,interval.end])
        l = sorted(l,key = lambda x:x[1])
        if not intervals:
            return True
        start = l[0][0]
        end = l[0][1]
        l = l[1:]

        for interval in l:
            if interval[0] < end:
                return False
            start = interval[0]
            end = interval[1]
        return True
            
            