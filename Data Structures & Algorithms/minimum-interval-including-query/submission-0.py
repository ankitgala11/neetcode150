class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        interval = [[p, q, q-p] for p, q in intervals]
        interval.sort(key = lambda x :x[2])

        ans = []


        for cnt, i in enumerate(queries):

            for p, q, d in interval:


                if p<= i and i<= q:
                  
                    ans.append(q-p+1)
                    break
        
            if len(ans)!=cnt+1:
                ans.append(-1)
            
        return ans
                
            

                
            