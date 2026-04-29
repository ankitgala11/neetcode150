class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        ans = 0


        for i in prices:
            if i < buy:
                buy = i
                
            else:
                sell = i
                if buy != float('inf'):
                    ans = max(ans, sell - buy)
                
        return ans
        