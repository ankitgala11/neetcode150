class Solution:
    def climbStairs(self, n: int) -> int:
        
        def solve(i):
            if i>=n:
                return 1
            if dp[i]!=-1:
                return dp[i]

            ans= solve(i+1) + solve(i+2)

            dp[i] = ans
            return ans
        
        dp = [-1]*(n+1)
        # return solve(1)

        def solveTab():
            dp = [0]*(n+2)
            dp[n]=1
            dp[n+1]=1

            for i in range(n-1, 0, -1):
                dp[i] = dp[i+1] + dp[i+2]

            return dp[1]

        return solveTab()
        
