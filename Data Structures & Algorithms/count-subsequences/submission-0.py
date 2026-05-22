class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n = len(s)
        m = len(t)

        def solve(i, j):
            
            if j>=m:
                return 1
            if i>=n:
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            op1 =op3=op2= 0
            if s[i] == t[j]:
                op1 = solve(i+1, j+1)
            op2 = solve(i+1, j)

            dp[(i,j)] =  (op1+op2)
            return dp[(i,j)]
        dp = {}
        return solve(0, 0)
            

