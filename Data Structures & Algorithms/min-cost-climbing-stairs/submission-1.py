class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # def solve(i):
        #     if i>=n:
        #         return 0
        #     if dp[i]!=float('inf'):
        #         return dp[i]

        #     ans = min(cost[i] + solve(i+1) , cost[i] + solve(i+2))

        #     dp[i] = ans
        #     return dp[i]

        n = len(cost)

        # dp = [float('inf')]*n
        # return min(solve(0), solve(1))

        def solveTab():
            dp = [float('inf')]*(n+2)

            dp[n]=0
            dp[n+1]=0

            for i in range(n-1, -1, -1):
                dp[i] = min(cost[i] + dp[i+1] , cost[i] + dp[i+2])
            
            return min(dp[0], dp[1])

        
        return solveTab()