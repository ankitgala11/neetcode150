class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(i, buy):
            if i >= n:
                return 0

            if dp[i][buy]!=-1:
                return dp[i][buy]

            buycond = sellcond = 0
            if buy:
                buycond = max(-prices[i] + solve(i+1, 0), solve(i+1, 1))
            
            else:
                sellcond = max( prices[i] + solve(i+2, 1), solve(i+1, 0))
            
            dp[i][buy]= max(buycond, sellcond)
            return dp[i][buy]
        
        dp = [[-1]*2 for _ in range(n)]
        return solve(0, 1)


            
