"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        interval = [[i.start, i.end] for i in intervals]
  
        if n <= 1:
            return n
        
        interval.sort()
       
        print(interval)
        last = []
        heapq.heappush(last , interval[0][1])
        
        for i in range(1, n):
            if last[0]> interval[i][0]:
                heapq.heappush(last , interval[i][1])
                
                
            
            else:
                heapq.heappop(last)
                heapq.heappush(last , interval[i][1])
                
            
        return len(last)