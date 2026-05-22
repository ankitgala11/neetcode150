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
        # dp = {}
        # return solve(0, 0)
        def solveTab():
            
            # dp = [[0]*(m+1) for _ in range(n+1)]
            curr = [0]*(m+1)
            next = [0]*(m+1)

            for i in range(n+1):
                curr[m]=1
                next[m]=1

            
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):

                    op1 =op3=op2= 0
                    if s[i] == t[j]:
                        op1 = next[j+1]
                    op2 = next[j]

                    curr[j] =  (op1+op2)
                next = curr[:]

            return curr[0]

        return solveTab()
            

