class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, n):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1] )
            
            else:
                ans.append(intervals[i])
            
        return ans