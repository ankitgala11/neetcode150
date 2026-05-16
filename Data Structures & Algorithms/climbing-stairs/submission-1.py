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
        return solve(1)