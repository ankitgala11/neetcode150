class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        n = len(intervals)

        while i<n:
            if intervals[i][0]<=newInterval[0]:
                i+=1
            else:
                break
            
        intervals.insert(i, newInterval)

        ans = [ intervals[0] ]


        for i in range(1, n+1):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1] )
            
            else:
                ans.append(intervals[i])
            
        return ans
