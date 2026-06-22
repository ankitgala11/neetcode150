"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key= lambda x: (x.start, x.end))

        heap = []

        for i in intervals:
            s=i.start
            e=i.end

            if heap and heap[0]<=s:
                heapq.heappop(heap)
                
            
            heapq.heappush(heap, e)
        
        return len(heap)
                