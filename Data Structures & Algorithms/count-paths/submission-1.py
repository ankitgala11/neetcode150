class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def solve(i, j):
            if i==m-1 and j==n-1:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]

            down=0
            right = 0
            if i+1<m:
                down = solve(i+1, j)
            if j+1<n:
                right = solve(i, j+1)

            dp[i][j]= down+right
            return dp[i][j]


        dp = [[-1]*n for _ in range(m)]
        return solve(0, 0)