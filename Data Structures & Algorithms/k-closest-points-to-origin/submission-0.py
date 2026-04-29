import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxh = []

        for x , y in points:

            dist = math.sqrt(x*x + y*y)

            heapq.heappush(maxh, (-dist, x, y))

            if len(maxh)>k:
                heapq.heappop(maxh)

        
        ans = []
        for dist, x, y in maxh:
            ans.append([x, y])

        
        return ans