import heapq
class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []
        self.median = 0

    
    def helper(self):
        if len(self.minh) < len(self.maxh): return 1
        elif len(self.minh) == len(self.maxh): return 0
        else: return -1


    def addNum(self, num: int) -> None:
        if self.helper() == 1:
            if num > self.median:
                heapq.heappush(self.minh, num)
            else:
                ele = heapq.heappop(self.maxh)
                heapq.heappush(self.maxh, -num)
                heapq.heappush(self.minh, -ele)
            self.median = (self.minh[0] + (-self.maxh[0]))/2

        elif self.helper() == 0:
            if num > self.median:
                heapq.heappush(self.minh, num)
                self.median = self.minh[0]
            else:
                heapq.heappush(self.maxh, -num)
                self.median = -self.maxh[0]
            

        else:
            if num > self.median:
                ele = heapq.heappop(self.minh)
                heapq.heappush(self.minh, num)
                heapq.heappush(self.maxh, -ele)
            else:
                heapq.heappush(self.maxh, -num)

            self.median = (self.minh[0] + (-self.maxh[0]))/2


    def findMedian(self) -> float:
        return self.median
        
        