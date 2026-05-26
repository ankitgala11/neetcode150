"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        n = len(intervals)
        interval = [[i.start, i.end] for i in intervals]
  
        if n <= 1:
            return True
        
        interval.sort()

        last = interval[0][1]
        
        for i in range(1, n):
            if last > interval[i][0]:
                return False
            
            else:
                last = interval[i][1]
            
        return True