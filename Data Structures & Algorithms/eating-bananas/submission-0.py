class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        s = 1
        e = max(piles)

        ans = -1
        n = len(piles)
        if h<n:return ans

        def issafe(m):

            cnt = 0

            for i in piles:
                cnt += math.ceil(i/m)
            
            if cnt>h:return False
            return True

        while s<=e:

            m = (s+e)//2

            if issafe(m):
                ans = m
                e = m -1

            
            else:
                s = m +1

        
        return ans
        