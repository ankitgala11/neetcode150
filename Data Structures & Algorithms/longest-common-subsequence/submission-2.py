class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)


        def solve(i, j):
            if i>=n or j>=m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            take=op1=op2 = 0

            if text1[i] == text2[j]:
                take = 1 + solve(i+1, j+1)

            else:
                op1 = solve(i+1, j)
                op2 = solve(i, j+1)

            dp[i][j]= max(take, op1, op2)
            return dp[i][j]
        
        # dp = [[-1]*m for _ in range(n)]
        # return solve(0, 0)
    
        def solveTabopt():
            # dp = [[0]*(m+1) for _ in range(n+1)]
            curr = [0]*(m+1)
            next = [0]*(m+1)
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):

                    take=op1=op2 = 0
                    if text1[i] == text2[j]:
                        take = 1 + next[j+1]

                    else:
                        op1 = next[ j]
                        op2 = curr[ j+1]

                    curr[j]= max(take, op1, op2)
                next = curr[:]
            return curr[0]
        
        
        return solveTabopt()