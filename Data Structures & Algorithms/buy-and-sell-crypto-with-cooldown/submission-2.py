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
        
        # dp = [[-1]*2 for _ in range(n)]
        # return solve(0, 1)


        def solveTabOpt():
            # dp = [[0]*2 for _ in range(n+2)]
            next2 = [0]*2
            next1 = [0]*2
            curr = [0]*2
            
            for i in range(n-1, -1, -1):
                for buy in range(2):

                    buycond = sellcond = 0
                    if buy:
                        buycond = max(-prices[i] + next1[0], next1[1])
                    
                    else:
                        sellcond = max( prices[i] + next2[1], next1[0])
                    
                    curr[buy]= max(buycond, sellcond)
                next2 = next1[:]
                next1 = curr[:]
            return curr[1]
        
        
        return solveTabOpt()


            
