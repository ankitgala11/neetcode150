import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        mp = {}

        for i in tasks:
            mp[i] = mp.get(i, 0) + 1

        minh = []
        for i , v in mp.items():
            heapq.heappush(minh, (0, -v, i))

        timer = 0

        while minh:


            currTimer , freq, task = heapq.heappop(minh)
            

            if currTimer <= timer:

                freq += 1
                if freq != 0:
                    heapq.heappush(minh, (currTimer+1+n, freq, task))
            
            
            else:
                
                timer = currTimer
                freq += 1
                if freq != 0:
                    heapq.heappush(minh, (currTimer+1+n, freq, task))
                
            timer += 1
          
        return timer


                

