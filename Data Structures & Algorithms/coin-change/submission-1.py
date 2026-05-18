class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # def solve(i, s):
        #     if i>=n or s>amount:
        #         return float('inf')
            
        #     if amount==s:
        #         return 0
            
        #     if dp[i][s]!=float('inf'):
        #         return dp[i][s]
            
        #     take = 1 + solve(i, s+coins[i])
        #     nottake = solve(i+1, s)
        
        #     dp[i][s]= min(take, nottake)
        #     return dp[i][s]

        
        # dp = [[float('inf')]*(amount+1) for _ in range(n)]
        # ans = solve(0, 0) 
        # if ans!= float('inf'):return ans
        # return -1

        def solveTab():
            dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
            
            for i in range(n+1):
                dp[i][amount]=0
            
            for i in range(n-1, -1, -1):
                for s in range(amount, -1, -1):
                    take=float('inf')
                    if s+coins[i]<=amount:
                        take = 1 + dp[i][s+coins[i]]
                    nottake = dp[i+1][s]
        
                    dp[i][s]= min(take, nottake)

            return dp[0][0]

        

        ans = solveTab() 
        if ans!= float('inf'):return ans
        return -1

