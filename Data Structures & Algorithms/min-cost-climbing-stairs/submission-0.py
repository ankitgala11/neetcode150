class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def solve(i):
            if i>=n:
                return 0
            if dp[i]!=float('inf'):
                return dp[i]

            ans = min(cost[i] + solve(i+1) , cost[i] + solve(i+2))

            dp[i] = ans
            return dp[i]

        n = len(cost)
        if n == 1:
            return cost[1]

        dp = [float('inf')]*n
        return min(solve(0), solve(1))