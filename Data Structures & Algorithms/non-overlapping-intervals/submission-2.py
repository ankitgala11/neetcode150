class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x:( x[1]))
        print(intervals)
        last = intervals[0][1]
        ans = 0
        for i in range(1, n):
            if last > intervals[i][0]:
                last = min(last, intervals[i][1])
                ans += 1
            
            else:
                last = intervals[i][1]
            
        return ans

 