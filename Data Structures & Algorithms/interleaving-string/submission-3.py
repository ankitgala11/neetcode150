class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n = len(s1)
        m = len(s2)
        l = len(s3)

        def solve(i, j, k):
            if k==l:
                if i==n and j==m:
                    return True
                else:
                    return False
                
            if dp[i][j][k]!=-1:
                return dp[i][j][k]

            if i<n and s1[i]==s3[k]:
                if solve(i+1, j, k+1):
                    dp[i][j][k]= True
                    return True
            
            if j<m and s2[j]==s3[k]:
                if solve(i, j+1, k+1):
                    dp[i][j][k]= True
                    return dp[i][j][k]

   
            dp[i][j][k]= False
            return False

        dp = [[[-1]*(1+l) for _ in range(m+1)]for _ in range(n+1)]
        return solve(0,0, 0)


            