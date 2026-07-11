class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        ans = float('-inf')

        while l<r:
            ans = max (ans , min(heights[l], heights[r])*(r-l))

            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        
        return ans
            
