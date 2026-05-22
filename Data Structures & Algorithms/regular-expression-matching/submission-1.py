class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def solve(i, j):

            if i>=n and j>=m:
                return True
            
            if j>=m and i<n:
                return False

            if dp[i][j]!=-1:
                return dp[i][j]

            op1=op2=op3=match =False
            if i<n and (s[i] == p[j] or p[j]=="."):
                match = True
            if match:
                op1 = solve(i+1, j+1)
            
            if j+1<m and p[j+1]=="*":

                op2 = solve(i, j+2) 
                if match:
                    op3 = solve(i+1, j)

            dp[i][j]= op1 or op2 or op3
            return dp[i][j]
        
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return solve(0, 0)