import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh = []

        for i in stones:
            heapq.heappush(maxh, -i)

        
        while(len(maxh) > 1):
            ele1 = heapq.heappop(maxh)
            ele1 = -ele1
            ele2 = heapq.heappop(maxh)
            ele2 = -ele2

            if ele1==ele2:
                heapq.heappush(maxh, 0)
            
            elif ele1<ele2:
                heapq.heappush(maxh, -(ele2 - ele1))

            else:
                heapq.heappush(maxh, -(ele1 - ele2))




        

        return -maxh[0]