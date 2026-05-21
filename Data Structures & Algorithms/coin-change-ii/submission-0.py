class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        def solve(i, s):
            if i>=n or s<0:
                return 0

            if s==0:
                return 1
            
            if dp[i][s]!=-1:
                return dp[i][s]
            
            take = solve(i, s-coins[i])
            nottake = solve(i+1, s)

            dp[i][s]= take + nottake
            return dp[i][s]


        dp = [[-1]*(amount+1) for _ in range(n)]
        return solve(0, amount)