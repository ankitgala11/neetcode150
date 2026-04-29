class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        
        ans = min(heights[l] , heights[r]) * (r-l)

        while l<r:
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

            ans = max(ans, min(heights[l] , heights[r]) * (r-l))
        
        return ans

            

        