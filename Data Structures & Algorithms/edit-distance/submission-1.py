class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        def solve(i, j):
            if i>=n and j>=m:
                return 0
            
            if i>=n and j<m:
                return m-j
            if j>=m and i<n:
                return n-i

            if dp[i][j]!=float('inf'):
                return dp[i][j]

            op1=op2=op3=op4=float('inf')
            if word1[i]==word2[j]:
                op4 = solve(i+1, j+1)
            
            else:
                op1 = 1 + solve(i+1, j)
                op2 = 1 + solve(i, j+1)
                op3 = 1+ solve(i+1, j+1)
            
            dp[i][j]= min(op1, op2, op3, op4)
            return dp[i][j]
        
        # dp = [[float('inf')]*m for _ in range(n)]
        # return solve(0, 0)

        def solveTab():
            dp = [[0]*(m+1) for _ in range(n+1)]
         
            for i in range(n+1):
                dp[i][m] = n-i
        
            for j in range(m+1):
                dp[n][j] = m-j
            
            for i in range(n-1 , -1, -1):
                for j in range(m-1, -1, -1):

                    op1=op2=op3=op4=float('inf')
                    if word1[i]==word2[j]:
                        op4 = dp[i+1][j+1]
                    
                    else:
                        op1 = 1 + dp[i+1][j]
                        op2 = 1 + dp[i][j+1]
                        op3 = 1+ dp[i+1][j+1]
            
                    dp[i][j]= min(op1, op2, op3, op4)
            return dp[0][0]
        
        
        return solveTab()